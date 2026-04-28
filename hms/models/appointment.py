class Appointment:
    def __init__(self, id, patient_id, doctor_id, appointment_date, appointment_time, status):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.status = status
