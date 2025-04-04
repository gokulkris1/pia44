from pia.voice.voice_input import record_audio, transcribe_audio
from pia.brains.router import ask
from voice.speak import speak

def run_voice_loop():
    print("🎧 Pia is listening... Speak after the beep.")
    record_audio()
    text = transcribe_audio()
    print("🗣 You said:", text)
    response = ask(text)
    print("Pia says:", response)
    speak(response)