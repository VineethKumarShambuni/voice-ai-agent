import re

def parse_intent(text: str):

    text = text.lower()

    intent = "unknown"

    if "book" in text:
        intent = "book_appointment"

    elif "cancel" in text:
        intent = "cancel_appointment"

    elif "reschedule" in text:
        intent = "reschedule_appointment"

    time_match = re.search(r"\d+\s*(am|pm)", text)

    time = time_match.group() if time_match else None

    return {
        "intent": intent,
        "time": time,
        "text": text
    }