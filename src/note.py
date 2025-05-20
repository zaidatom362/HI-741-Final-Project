# note.py
# Represents a clinical note for a visit

class Note:
    """A clinical note attached to a visit."""
    def __init__(self, note_id, note_type=None, visit_id=None, note_text=""):
        self.note_id = note_id
        self.note_type = note_type
        self.visit_id = visit_id
        self.note_text = note_text
