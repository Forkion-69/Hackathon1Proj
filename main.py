"""Kisan Voice: IVR logic + Twilio webhooks + browser phone simulator.
Run: uvicorn main:app --reload   (open http://localhost:8000)"""
import hashlib, html, os
from pathlib import Path
from urllib.parse import quote
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, Response
from pydantic import BaseModel
from data import T, CROPS, PRICES, MANDI, LANGS, RS

BASE = os.getenv("BASE_URL", "http://localhost:8000")  # set to your ngrok URL for Twilio
CACHE = Path("audio_cache"); CACHE.mkdir(exist_ok=True)
app = FastAPI(title="Kisan Voice")
SESSIONS = {}  # call id -> {"lang":..., "node":...}
NEXT = {"1": "crop", "2": "schemes", "3": "well"}


def say(text, lang): return {"text": text, "lang": lang}
def new_session(): return {"lang": None, "node": "lang"}


def prompt(s):
    if s["node"] == "lang":
        return [say(T["lang"][l], l) for l in LANGS.values()]
    return [say(T["menu_" + s["node"]][s["lang"]], s["lang"])]


def price_text(d, lang):
    key, names = CROPS[d]
    lines = ", ".join(f"{MANDI[m][lang]} {p} {RS[lang]}" for m, p in PRICES[key].items())
    return T["price"][lang].format(crop=names[lang], lines=lines)


def step(s, d):
    """Pure menu logic: (session, digit) -> list of things to say. No telephony here."""
    node, lang, answer = s["node"], s["lang"], []
    invalid = [say(T["invalid"][lang or "en"], lang or "en")]
    if node == "lang":
        if d in LANGS: s["lang"], s["node"] = LANGS[d], "main"
    elif d == "0":
        s["node"] = "lang" if node == "main" else "main"
    elif d == "9" or not d:
        pass  # repeat current menu
    elif node == "main":
        if d in NEXT: s["node"] = NEXT[d]
        else: answer = invalid
    elif node == "crop" and d in CROPS:
        answer = [say(price_text(d, lang), lang)]
    elif node == "schemes" and d in "1234":
        answer = [say(T["s_" + d][lang], lang)]
    elif node == "well" and d in ("1", "2"):
        answer = [say(T["well_" + d][lang], lang)]
    else:
        answer = invalid
    return answer + prompt(s)


def audio_url(seg, base=""):
    return f"{base}/tts?lang={seg['lang']}&text={quote(seg['text'])}"


@app.get("/tts")
def tts(text: str, lang: str = "en"):
    f = CACHE / (hashlib.md5(f"{lang}{text}".encode()).hexdigest() + ".mp3")
    if not f.exists():
        from gtts import gTTS
        gTTS(text, lang=lang).save(str(f))
    return FileResponse(f, media_type="audio/mpeg")


# ---- Twilio voice webhooks -------------------------------------------------
def twiml(segs):
    plays = "".join(f"<Play>{html.escape(audio_url(x, BASE))}</Play>" for x in segs)
    xml = (f'<?xml version="1.0" encoding="UTF-8"?><Response>'
           f'<Gather numDigits="1" timeout="7" action="{BASE}/voice/step" method="POST">{plays}</Gather>'
           f'<Redirect method="POST">{BASE}/voice/step</Redirect></Response>')
    return Response(xml, media_type="text/xml")


@app.post("/voice")
def voice_start(CallSid: str = Form(...)):
    SESSIONS[CallSid] = new_session()
    return twiml(prompt(SESSIONS[CallSid]))


@app.post("/voice/step")
def voice_step(CallSid: str = Form(...), Digits: str = Form("")):
    s = SESSIONS.setdefault(CallSid, new_session())
    return twiml(step(s, Digits))


# ---- Browser simulator (demo fallback, no telephony needed) -----------------
class Sim(BaseModel):
    sid: str
    digit: str = ""


@app.post("/sim/step")
def sim_step(b: Sim):
    fresh = b.sid not in SESSIONS
    s = SESSIONS.setdefault(b.sid, new_session())
    segs = prompt(s) if fresh else step(s, b.digit)
    return [{**x, "audio": audio_url(x)} for x in segs]


@app.get("/")
def home(): return FileResponse("static/simulator.html")
