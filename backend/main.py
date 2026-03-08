from services.text_to_speech.tts_service import generate_voice
from memory.session_memory.memory_manager import store_message, get_session
from fastapi import FastAPI, UploadFile, File
import shutil
import whisper

from agent.reasoning.intent_parser import parse_intent
from scheduler.appointment_engine.appointment_manager import create_appointment, cancel_appointment

app = FastAPI()

model = whisper.load_model("tiny")

@app.post("/voice-command")
async def voice_command(session_id: str, file: UploadFile = File(...)):

    file_path = "temp_audio.wav"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = model.transcribe(file_path)

    text = result["text"]

    intent = parse_intent(text)

    response = {}
    voice_file = generate_voice(response["message"])

    if intent["intent"] == "book_appointment":
        response = create_appointment(intent["time"], text)

    elif intent["intent"] == "cancel_appointment":
        response = cancel_appointment(intent["time"])

    else:
        response = {"message": "No valid action detected"}

    return {
        "transcription": text,
        "intent": intent,
        "response": response,
        "voice_response_file": voice_file,
        "conversation_history": history
    } 