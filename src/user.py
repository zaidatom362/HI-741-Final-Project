
# Represents a user and their allowed actions
# user.py

class User:
    """A user with a role and permission checking."""
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def can_perform(self, action):
        permissions = {
            'admin': ['count_visits', 'generate_statistics'],
            'clinician': ['add_patient', 'remove_patient', 'retrieve_patient', 'view_note', 'count_visits'],
            'nurse': ['add_patient', 'remove_patient', 'retrieve_patient', 'view_note', 'count_visits'],
            'management': ['generate_statistics']
        }
        return action in permissions.get(self.role, [])
