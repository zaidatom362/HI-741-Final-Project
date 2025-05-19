# visit.py
# Represents a single patient visit

class Visit:
    """Stores details of a patient visit."""
    def __init__(self, visit_id, visit_time, department, gender, race, age, ethnicity, insurance, zip_code, chief_complaint):
        self.visit_id = visit_id
        self.visit_time = visit_time  # string, e.g. "2024-05-18"
        self.department = department
        self.gender = gender
        self.race = race
        self.age = age
        self.ethnicity = ethnicity
        self.insurance = insurance
        self.zip_code = zip_code
        self.chief_complaint = chief_complaint
