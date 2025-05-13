# customer_patient.py

"""
customer_patient.py - Models a patient with associated visits and notes.
"""

from typing import List, Optional
from appointment_visit import AppointmentVisit
from clinical_note import ClinicalNote

class CustomerPatient:
    """
    Represents a patient record, holding multiple visits and clinical notes.
    """

    def __init__(self, patient_id: str):
        """
        Args:
            patient_id: Unique identifier for this patient.
        """
        self.patient_id: str = patient_id
        self.visits: List[AppointmentVisit] = []
        self.notes: List[ClinicalNote] = []

    def add_visit(self, visit: AppointmentVisit) -> None:
        """
        Add a new visit to this patient's record.

        Args:
            visit: An AppointmentVisit instance.
        """
        self.visits.append(visit)

    def add_note(self, note: ClinicalNote) -> None:
        """
        Attach a clinical note to this patient.

        Args:
            note: A ClinicalNote instance.
        """
        self.notes.append(note)

    def get_most_recent_visit(self) -> Optional[AppointmentVisit]:
        """
        Return the most recent visit, based on its timestamp.

        Returns:
            The AppointmentVisit with the greatest 'time' attribute, or None.
        """
        if not self.visits:
            return None
        return max(self.visits, key=lambda v: v.time)

    def get_notes_by_date(self, date_str: str) -> List[ClinicalNote]:
        """
        Retrieve all clinical notes whose VisitID begins with the given date.

        Args:
            date_str: Date prefix in YYYY-MM-DD format.
        Returns:
            List of ClinicalNote instances for that date.
        """
        return [note for note in self.notes if note.visit_id.startswith(date_str)]
