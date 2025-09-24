from flask import Flask, render_template, request, jsonify
import re
from datetime import datetime

app = Flask(__name__)

class HospitalChatbot:
    def __init__(self):
        self.intents = {
            'greeting': r'\b(hi|hello|hey|greetings)\b',
            'appointment': r'\b(appointment|book|schedule|consult)\b',
            'doctors': r'\b(doctor|specialist|physician|consultation|dr|medical team|doctors|specialists)\b',
            'timing': r'\b(timing|hours|open|close|schedule|when)\b',
            'emergency': r'\b(emergency|urgent|ambulance|critical)\b',
            'location': r'\b(location|address|where|find|direction|map|reach|get there|parking|transport)\b',
            'location_specific': r'\b(bus|metro|train|car|parking|route|direction from)\b',
            'facilities': r'\b(facilities|services|equipment|treatment|offer|details|more|explain|tell me more|what|deep)\b',
            'department': r'\b(department|ward|unit|section)\b',
            'pharmacy': r'\b(pharmacy|medicine|drug|prescription|medical shop)\b'
        }
        
    def get_response(self, message):
        message = message.lower()
        
        if re.search(self.intents['greeting'], message):
            return ("👋 Welcome to Raksha Hospital!\n\n"
                   "How can I help you?\n"
                   "• Appointments\n"
                   "• Doctors\n"
                   "• Timings\n"
                   "• Emergency\n"
                   "• Location\n"
                   "• Pharmacy")
            
        elif re.search(self.intents['appointment'], message):
            return ("📅 Book Appointment:\n\n"
                   "Please provide:\n"
                   "1. Name\n"
                   "2. Phone\n"
                   "3. Date\n"
                   "4. Time: Morning (9AM-1PM) or Evening (4PM-8PM)\n"
                   "5. Department")
            
        elif re.search(self.intents['doctors'], message):
            return ("👨‍⚕️ Our Doctors:\n\n"
                   "General Medicine:\n"
                   "• Dr. Sarah (Mon-Wed)\n"
                   "• Dr. Michael (Thu-Sat)\n\n"
                   "Cardiology:\n"
                   "• Dr. Robert (Mon-Fri)\n"
                   "• Dr. Emily (Sat)\n\n"
                   "Pediatrics:\n"
                   "• Dr. Lisa (Mon-Wed)\n"
                   "• Dr. David (Thu-Sat)")
            
        elif re.search(self.intents['timing'], message):
            return ("⏰ Timings:\n\n"
                   "OPD: Mon-Fri (8AM-8PM)\n"
                   "Sat (8AM-6PM)\n"
                   "Sun (9AM-1PM)\n\n"
                   "Emergency & Pharmacy: 24/7\n"
                   "Lab: 7AM-9PM daily")
            
        elif re.search(self.intents['emergency'], message):
            return ("🚨 Emergency:\n\n"
                   "Hotline: 8838781822\n"
                   "Ambulance: 108\n"
                   "Reception: 9976139000\n\n"
                   "24/7 Emergency Services Available")
            
        elif re.search(self.intents['location'], message):
            if 'parking' in message:
                return ("🅿️ Parking Information:\n\n"
                       "• 24/7 secure parking available\n"
                       "• Valet parking (8AM-8PM)\n"
                       "• Free parking for emergency cases\n"
                       "• Dedicated spots for differently-abled\n\n"
                       "Would you like directions to the parking area?")
            
            elif any(x in message for x in ['bus', 'metro', 'train', 'transport']):
                return ("🚌 Public Transport Options:\n\n"
                       "Bus Routes:\n"
                       "• 101 from City Center\n"
                       "• 102 from Railway Station\n"
                       "• 103 from Airport\n\n"
                       "Metro:\n"
                       "• Nearest: Central Metro Station (2 min walk)\n"
                       "• Exit from Gate 2\n\n"
                       "Need more specific directions?")
            
            else:
                return ("📍 Raksha Hospital Location:\n\n"
                       "Address: 123 Healthcare Avenue\n"
                       "Landmark: Near Central Metro\n\n"
                       "Quick Directions:\n"
                       "• From City Center: 10 mins\n"
                       "• From Airport: 30 mins\n"
                       "• From Railway Station: 15 mins\n\n"
                       "Need specific transport options or parking information?")
            
        elif re.search(self.intents['pharmacy'], message):
            return ("💊 Pharmacy (24/7):\n\n"
                   "• All medicines available\n"
                   "• Counter: 9876543210\n"
                   "• WhatsApp: 8765432109\n"
                   "• Home delivery available\n"
                   "• Prescription required for medicines")
            
        else:
            return ("I don't understand. Please ask about:\n"
                   "• Appointments\n"
                   "• Doctors\n"
                   "• Timings\n"
                   "• Emergency\n"
                   "• Location\n"
                   "• Pharmacy")

chatbot = HospitalChatbot()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat")
def chat_page():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message")
    if not message:
        return jsonify({"reply": "Please enter a message."})

    reply = chatbot.get_response(message)
    return jsonify({"reply": reply})

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)