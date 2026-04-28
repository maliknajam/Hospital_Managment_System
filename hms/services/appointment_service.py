from hms.utils.db import execute_query
from hms.models.appointment import Appointment

class AppointmentService:
    @staticmethod
    def get_all_appointments():
        query = """
        SELECT a.id, a.patient_id, a.doctor_id, a.appointment_date, a.appointment_time, a.status,
               p.name as patient_name, d.name as doctor_name
        FROM appointments a
        JOIN patients p ON a.patient_id = p.id
        JOIN doctors d ON a.doctor_id = d.id
        """
        return execute_query(query, fetch=True)

    @staticmethod
    def add_appointment(patient_id, doctor_id, appointment_date, appointment_time, status='Scheduled'):
        query = """
        INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, status) 
        VALUES (?, ?, ?, ?, ?)
        """
        return execute_query(query, (patient_id, doctor_id, appointment_date, appointment_time, status))

    @staticmethod
    def update_appointment(appointment_id, patient_id, doctor_id, appointment_date, appointment_time, status):
        query = """
        UPDATE appointments 
        SET patient_id=?, doctor_id=?, appointment_date=?, appointment_time=?, status=? 
        WHERE id=?
        """
        execute_query(query, (patient_id, doctor_id, appointment_date, appointment_time, status, appointment_id))

    @staticmethod
    def delete_appointment(appointment_id):
        query = "DELETE FROM appointments WHERE id=?"
        execute_query(query, (appointment_id,))
