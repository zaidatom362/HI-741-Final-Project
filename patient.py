# patient.py
# Represents a patient with their visits and notes

class Patient:
    """A patient with a list of visits and notes."""
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.visits = []
        self.notes = []

    def add_visit(self, visit):
        """Attach a visit to this patient."""
        self.visits.append(visit)

    def add_note(self, note):
        """Attach a note to this patient."""
        self.notes.append(note)
