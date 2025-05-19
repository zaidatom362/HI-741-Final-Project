# department.py
# Represents a hospital department and its patients

class Department:
    """A department contains a set of patients."""
    def __init__(self, name):
        self.name = name
        self.patients = set()

    def add_patient(self, patient):
        """Add a patient to this department."""
        self.patients.add(patient)

    def remove_patient(self, patient):
        """Remove a patient if present."""
        self.patients.discard(patient)
