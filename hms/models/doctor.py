class Doctor:
    def __init__(self, id, name, specialty, contact_number, availability, created_at=None):
        self.id = id
        self.name = name
        self.specialty = specialty
        self.contact_number = contact_number
        self.availability = availability
        self.created_at = created_at
