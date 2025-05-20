
# Represents a patient with their visits and notes

# patient.py

class Patient:
    """A patient with a list of visits and notes."""
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.visits = []
        self.notes = []

    def add_visit(self, visit):
        self.visits.append(visit)

    def add_note(self, note):
        self.notes.append(note)
