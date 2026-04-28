from hms.utils.db import execute_query
from hms.models.billing import Billing

class BillingService:
    @staticmethod
    def get_all_bills():
        query = """
        SELECT b.id, b.patient_id, b.amount, b.status, b.billing_date, p.name as patient_name
        FROM billing b
        JOIN patients p ON b.patient_id = p.id
        """
        return execute_query(query, fetch=True)

    @staticmethod
    def add_bill(patient_id, amount, status, billing_date):
        query = """
        INSERT INTO billing (patient_id, amount, status, billing_date) 
        VALUES (?, ?, ?, ?)
        """
        return execute_query(query, (patient_id, amount, status, billing_date))

    @staticmethod
    def update_bill(bill_id, patient_id, amount, status, billing_date):
        query = """
        UPDATE billing 
        SET patient_id=?, amount=?, status=?, billing_date=? 
        WHERE id=?
        """
        execute_query(query, (patient_id, amount, status, billing_date, bill_id))

    @staticmethod
    def delete_bill(bill_id):
        query = "DELETE FROM billing WHERE id=?"
        execute_query(query, (bill_id,))
