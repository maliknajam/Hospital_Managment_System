class Patient:
    def __init__(self, id, name, age, gender, contact_number, address, created_at=None):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_number = contact_number
        self.address = address
        self.created_at = created_at
