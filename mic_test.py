import sounddevice as sd
from scipy.io.wavfile import write
import whisper

from agent.reasoning.intent_parser import parse_intent
from scheduler.appointment_engine.appointment_manager import create_appointment, cancel_appointment

fs = 16000
seconds = 5

print("🎤 Speak now...")

recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

write("mic_audio.wav", fs, recording)

print("Recording finished")

model = whisper.load_model("tiny")

result = model.transcribe("mic_audio.wav")

text = result["text"]

print("Transcription:", text)

intent = parse_intent(text)

print("Detected Intent:", intent)

if intent["intent"] == "book_appointment":
    response = create_appointment(intent["time"], text)
    print(response)

elif intent["intent"] == "cancel_appointment":
    response = cancel_appointment(intent["time"])
    print(response)

else:
    print("No action detected")