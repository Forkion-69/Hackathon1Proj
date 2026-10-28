"""Mock data + all spoken text. Edit freely: add languages/crops/schemes here."""
LANGS = {"1": "mr", "2": "hi", "3": "en"}
RS = {"mr": "रुपये", "hi": "रुपये", "en": "rupees"}

MANDI = {
    "pune": {"mr": "पुणे", "hi": "पुणे", "en": "Pune"},
    "nashik": {"mr": "नाशिक", "hi": "नाशिक", "en": "Nashik"},
    "nagpur": {"mr": "नागपूर", "hi": "नागपुर", "en": "Nagpur"},
    "latur": {"mr": "लातूर", "hi": "लातूर", "en": "Latur"},
    "kolhapur": {"mr": "कोल्हापूर", "hi": "कोल्हापुर", "en": "Kolhapur"},
}
CROPS = {  # digit -> (key, names)
    "1": ("onion", {"mr": "कांदा", "hi": "प्याज", "en": "onion"}),
    "2": ("soybean", {"mr": "सोयाबीन", "hi": "सोयाबीन", "en": "soybean"}),
    "3": ("cotton", {"mr": "कापूस", "hi": "कपास", "en": "cotton"}),
    "4": ("tur", {"mr": "तूर", "hi": "तुअर", "en": "tur"}),
}
PRICES = {  # MOCK prices, rupees per quintal
    "onion": {"nashik": 1720, "pune": 1850, "kolhapur": 1790},
    "soybean": {"latur": 4650, "nagpur": 4580, "pune": 4700},
    "cotton": {"nagpur": 7100, "latur": 7050, "nashik": 7200},
    "tur": {"latur": 7400, "nagpur": 7350, "kolhapur": 7500},
}

T = {
 "lang": {"mr": "मराठीसाठी 1 दाबा.", "hi": "हिंदी के लिए 2 दबाएं.", "en": "For English, press 3."},
 "invalid": {"mr": "चुकीचा पर्याय. कृपया पुन्हा प्रयत्न करा.", "hi": "गलत विकल्प. कृपया फिर कोशिश करें.", "en": "Invalid option. Please try again."},
 "menu_main": {
  "mr": "बाजारभावासाठी 1 दाबा. सरकारी योजनांसाठी 2 दाबा. मानसिक आधारासाठी 3 दाबा. पुन्हा ऐकण्यासाठी 9 दाबा.",
  "hi": "मंडी भाव के लिए 1 दबाएं. सरकारी योजनाओं के लिए 2 दबाएं. मानसिक सहयोग के लिए 3 दबाएं. दोबारा सुनने के लिए 9 दबाएं.",
  "en": "For market prices, press 1. For government schemes, press 2. For emotional support, press 3. To repeat, press 9."},
 "menu_crop": {
  "mr": "कांद्यासाठी 1, सोयाबीनसाठी 2, कापसासाठी 3, तुरीसाठी 4 दाबा. मागे जाण्यासाठी 0 दाबा.",
  "hi": "प्याज के लिए 1, सोयाबीन के लिए 2, कपास के लिए 3, तुअर के लिए 4 दबाएं. पीछे जाने के लिए 0 दबाएं.",
  "en": "Onion, press 1. Soybean, 2. Cotton, 3. Tur, 4. To go back, press 0."},
 "menu_schemes": {
  "mr": "पीएम किसानसाठी 1, नमो शेतकरी निधीसाठी 2, पीक विम्यासाठी 3, किसान क्रेडिट कार्डसाठी 4 दाबा. मागे जाण्यासाठी 0 दाबा.",
  "hi": "पीएम किसान के लिए 1, नमो शेतकरी निधि के लिए 2, फसल बीमा के लिए 3, किसान क्रेडिट कार्ड के लिए 4 दबाएं. पीछे जाने के लिए 0 दबाएं.",
  "en": "PM-Kisan, press 1. Namo Shetkari fund, 2. Crop insurance, 3. Kisan Credit Card, 4. To go back, press 0."},
 "menu_well": {
  "mr": "मदतीच्या हेल्पलाइनसाठी 1 दाबा. मन शांत करणाऱ्या संदेशासाठी 2 दाबा. मागे जाण्यासाठी 0 दाबा.",
  "hi": "सहायता हेल्पलाइन के लिए 1 दबाएं. मन शांत करने वाले संदेश के लिए 2 दबाएं. पीछे जाने के लिए 0 दबाएं.",
  "en": "For a free helpline, press 1. For a calming message, press 2. To go back, press 0."},
 "price": {
  "mr": "{crop} चा आजचा भाव प्रति क्विंटल: {lines}.",
  "hi": "{crop} का आज का भाव प्रति क्विंटल: {lines}.",
  "en": "Today's {crop} price per quintal: {lines}."},
 "s_1": {"mr": "पीएम किसान योजनेत पात्र शेतकऱ्यांना वर्षाला 6000 रुपये, तीन हप्त्यांत मिळतात.",
         "hi": "पीएम किसान योजना में पात्र किसानों को साल में 6000 रुपये, तीन किस्तों में मिलते हैं.",
         "en": "Under PM-Kisan, eligible farmers get 6000 rupees a year in three installments."},
 "s_2": {"mr": "नमो शेतकरी महासन्मान निधी अंतर्गत महाराष्ट्र सरकार पात्र शेतकऱ्यांना वर्षाला अतिरिक्त 6000 रुपये देते.",
         "hi": "नमो शेतकरी महासम्मान निधि के तहत महाराष्ट्र सरकार पात्र किसानों को सालाना 6000 रुपये अतिरिक्त देती है.",
         "en": "Under the Namo Shetkari Mahasanman Nidhi, Maharashtra adds another 6000 rupees a year for eligible farmers."},
 "s_3": {"mr": "पीक विमा योजना नैसर्गिक आपत्तीमुळे पिकाचे नुकसान झाल्यास विमा संरक्षण देते.",
         "hi": "फसल बीमा योजना प्राकृतिक आपदा से फसल के नुकसान पर बीमा सुरक्षा देती है.",
         "en": "Crop insurance protects you if natural disasters damage your crop."},
 "s_4": {"mr": "किसान क्रेडिट कार्डमुळे शेतीसाठी कमी व्याजदराने कर्ज मिळते.",
         "hi": "किसान क्रेडिट कार्ड से खेती के लिए कम ब्याज पर कर्ज मिलता है.",
         "en": "The Kisan Credit Card gives low-interest loans for farming."},
 "well_1": {"mr": "तुम्ही एकटे नाही आहात. मोफत मानसिक आधारासाठी, 24 तास, 14416 वर कॉल करा.",
            "hi": "आप अकेले नहीं हैं. मुफ़्त मानसिक सहयोग के लिए, 24 घंटे, 14416 पर कॉल करें.",
            "en": "You are not alone. For free support, any time of day, call 14416."},
 "well_2": {"mr": "एक दीर्घ श्वास घ्या आणि हळूहळू सोडा. मनातलं बोलल्याने हलकं वाटतं. गरज वाटल्यास 14416 वर कॉल करा.",
            "hi": "एक गहरी सांस लें और धीरे धीरे छोड़ें. मन की बात करने से हल्का लगता है. ज़रूरत हो तो 14416 पर कॉल करें.",
            "en": "Take a slow, deep breath. Talking helps. If you need to, call 14416."},
}
