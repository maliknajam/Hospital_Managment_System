from hms.utils.db import execute_query
from hms.models.medical_record import MedicalRecord

class MedicalRecordService:
    @staticmethod
    def get_all_records():
        query = """
        SELECT mr.id, mr.patient_id, mr.doctor_id, mr.diagnosis, mr.prescription, mr.notes, mr.record_date,
               p.name as patient_name, d.name as doctor_name
        FROM medical_records mr
        JOIN patients p ON mr.patient_id = p.id
        JOIN doctors d ON mr.doctor_id = d.id
        """
        return execute_query(query, fetch=True)

    @staticmethod
    def add_record(patient_id, doctor_id, diagnosis, prescription, notes, record_date):
        query = """
        INSERT INTO medical_records (patient_id, doctor_id, diagnosis, prescription, notes, record_date) 
        VALUES (?, ?, ?, ?, ?, ?)
        """
        return execute_query(query, (patient_id, doctor_id, diagnosis, prescription, notes, record_date))

    @staticmethod
    def update_record(record_id, patient_id, doctor_id, diagnosis, prescription, notes, record_date):
        query = """
        UPDATE medical_records 
        SET patient_id=?, doctor_id=?, diagnosis=?, prescription=?, notes=?, record_date=? 
        WHERE id=?
        """
        execute_query(query, (patient_id, doctor_id, diagnosis, prescription, notes, record_date, record_id))

    @staticmethod
    def delete_record(record_id):
        query = "DELETE FROM medical_records WHERE id=?"
        execute_query(query, (record_id,))
