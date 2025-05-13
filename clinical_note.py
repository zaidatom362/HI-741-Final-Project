"""
clinical_note.py - Single note attached to a visit.
"""
class ClinicalNote:
    def __init__(self, nid, vid, text):
        self.id       = nid
        self.visit_id = vid
        self.text     = text
