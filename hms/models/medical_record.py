class MedicalRecord:
    def __init__(self, id, patient_id, doctor_id, diagnosis, prescription, notes, record_date):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.diagnosis = diagnosis
        self.prescription = prescription
        self.notes = notes
        self.record_date = record_date
