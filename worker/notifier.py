# worker/notifier.py

import json
from twilio.rest import Client

def load_config():
    with open("config.json") as f:
        return json.load(f)

def send_whatsapp_alert(message: str):
    config = load_config()
    if not config.get("send_whatsapp"):
        return

    client = Client(config["twilio_account_sid"], config["twilio_auth_token"])

    try:
        msg = client.messages.create(
            body=message,
            from_="whatsapp:+14155238886",  # Twilio sandbox
            to=f"whatsapp:{config['whatsapp_number']}"
        )
        print(f"✅ WhatsApp message sent: {msg.sid}")
    except Exception as e:
        print(f"❌ Failed to send WhatsApp message: {e}")