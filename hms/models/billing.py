class Billing:
    def __init__(self, id, patient_id, amount, status, billing_date):
        self.id = id
        self.patient_id = patient_id
        self.amount = amount
        self.status = status
        self.billing_date = billing_date
