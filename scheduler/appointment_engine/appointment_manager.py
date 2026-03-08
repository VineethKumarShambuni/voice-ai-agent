appointments = []

def create_appointment(time, text):

    appointment = {
        "time": time,
        "details": text
    }

    appointments.append(appointment)

    return {
        "status": "success",
        "message": f"Appointment booked at {time}"
    }


def cancel_appointment(time):

    global appointments

    appointments = [a for a in appointments if a["time"] != time]

    return {
        "status": "success",
        "message": f"Appointment at {time} cancelled"
    }


def list_appointments():

    return appointments