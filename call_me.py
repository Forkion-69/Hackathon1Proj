import os
from twilio.rest import Client

client = Client(os.environ["TWILIO_SID"], os.environ["TWILIO_TOKEN"])
call = client.calls.create(
       to="+919850707953",      
       from_="+17372508034",   
       url=os.environ["BASE_URL"] + "/voice",
       
   )
print(call.sid)  