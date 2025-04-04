import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ELEVEN_API_KEY")
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"

def speak(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        os.makedirs("voice", exist_ok=True)
        with open("voice/pia_voice.mp3", "wb") as f:
            f.write(response.content)
        os.system("start voice/pia_voice.mp3" if os.name == "nt" else "ffplay -nodisp -autoexit voice/pia_voice.mp3")
    else:
        print("Voice generation failed:", response.text)