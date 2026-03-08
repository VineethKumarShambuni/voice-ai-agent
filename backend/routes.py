from fastapi import APIRouter
from agent.intent_agent import detect_intent
from scheduler.appointment_engine import book_appointment
from memory.session_memory import save_session

router = APIRouter()

@router.post("/agent")
def agent_request(user_text: str, session_id: str):

    intent_data = detect_intent(user_text)

    save_session(session_id, intent_data)

    if intent_data["intent"] == "book":
        result = book_appointment(intent_data["doctor"], intent_data["date"])
        return {"response": result}

    return {"response": "Intent not supported yet"}