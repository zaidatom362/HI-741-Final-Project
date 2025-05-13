"""
appointment_visit.py - Stores a single visit's data.
"""
class AppointmentVisit:
    def __init__(self, vid, vtime, dept, gender, race,
                 age, ethnicity, insurance, zipc, complaint):
        self.id         = vid
        self.time       = vtime
        self.department = dept
        self.gender     = gender
        self.race       = race
        self.age        = age
        self.ethnicity  = ethnicity
        self.insurance  = insurance
        self.zip        = zipc
        self.complaint  = complaint
