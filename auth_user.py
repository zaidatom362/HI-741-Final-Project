"""
auth_user.py - User with role‐based permissions.
"""
class AuthUser:
    def __init__(self, name, role, login_time):
        self.name = name
        self.role = role
        self.login_time = login_time

    def permissions(self):
        perms = {
            'admin':       ['count_visits'],
            'clinician':   ['add_patient','remove_patient','retrieve_patient','view_note','count_visits'],
            'nurse':       ['add_patient','remove_patient','retrieve_patient','view_note','count_visits'],
            'management':  ['generate_statistics']
        }
        return perms.get(self.role, [])
