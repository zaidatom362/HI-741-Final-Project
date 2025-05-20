# department.py

class Department:
    """A department contains a set of patients."""
    def __init__(self, name):
        self.name = name
        self.patients = set()

    def add_patient(self, patient):
        self.patients.add(patient)

    def remove_patient(self, patient):
        self.patients.discard(patient)
