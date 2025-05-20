# utils.py
# Authentication utility for the hospital system
import csv
import os

def authenticate(username, password):
    """Return user role if credentials match, else None."""
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'Credentials.csv')
    try:
        with open(path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username and row['password'] == password:
                    return row['role']
    except FileNotFoundError:
        print("Credential file not found.")
    return None
