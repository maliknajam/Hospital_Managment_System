from hms.utils.db import execute_query
from hms.models.doctor import Doctor

class DoctorService:
    @staticmethod
    def get_all_doctors():
        query = "SELECT * FROM doctors"
        results = execute_query(query, fetch=True)
        return [Doctor(**row) for row in results]

    @staticmethod
    def add_doctor(name, specialty, contact_number, availability):
        query = """
        INSERT INTO doctors (name, specialty, contact_number, availability) 
        VALUES (?, ?, ?, ?)
        """
        return execute_query(query, (name, specialty, contact_number, availability))

    @staticmethod
    def update_doctor(doctor_id, name, specialty, contact_number, availability):
        query = """
        UPDATE doctors 
        SET name=?, specialty=?, contact_number=?, availability=? 
        WHERE id=?
        """
        execute_query(query, (name, specialty, contact_number, availability, doctor_id))

    @staticmethod
    def delete_doctor(doctor_id):
        query = "DELETE FROM doctors WHERE id=?"
        execute_query(query, (doctor_id,))
