import os
import openai
import sounddevice as sd
from scipy.io.wavfile import write
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def record_audio(filename="voice/input.wav", duration=5, fs=44100):
    print("🎙 Recording... Speak now.")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    os.makedirs("voice", exist_ok=True)
    write(filename, fs, audio)
    print("✅ Recording saved.")

def transcribe_audio(filename="voice/input.wav"):
    with open(filename, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]