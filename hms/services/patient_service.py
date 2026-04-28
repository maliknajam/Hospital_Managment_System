from hms.utils.db import execute_query
from hms.models.patient import Patient

class PatientService:
    @staticmethod
    def get_all_patients():
        query = "SELECT * FROM patients"
        results = execute_query(query, fetch=True)
        return [Patient(**row) for row in results]

    @staticmethod
    def add_patient(name, age, gender, contact_number, address):
        query = """
        INSERT INTO patients (name, age, gender, contact_number, address) 
        VALUES (?, ?, ?, ?, ?)
        """
        return execute_query(query, (name, age, gender, contact_number, address))

    @staticmethod
    def update_patient(patient_id, name, age, gender, contact_number, address):
        query = """
        UPDATE patients 
        SET name=?, age=?, gender=?, contact_number=?, address=? 
        WHERE id=?
        """
        execute_query(query, (name, age, gender, contact_number, address, patient_id))

    @staticmethod
    def delete_patient(patient_id):
        query = "DELETE FROM patients WHERE id=?"
        execute_query(query, (patient_id,))
