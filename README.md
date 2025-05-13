# HI-741-Final-Project
Hospital Management System
==========================

A role-based clinical data warehouse with a user-friendly Tkinter UI for managing patient visits, notes, and key statistics.

Overview
--------
Supports four user roles-clinician, nurse, admin, and management-each with a customized menu of actions:

• Clinician & Nurse:
  - Add Patient  
  - Remove Patient  
  - Retrieve Patient  
  - Count Visits  
  - View Note  

• Admin:
  - Count Visits  

• Management:
  - Generate Key Statistics  
  - Count Visits  

All changes update the master patient file, clinical notes are linked by visit date, and every action is logged for auditing.

Features
--------
- Secure login using fixed-width credentials  
- Role-based menus enforcing access rules  
- Add, remove, and retrieve patient visits  
- View clinical notes by date  
- Count daily visits  
- Generate and save visit-trend bar charts  
- Audit logging of all user actions  

Project Structure
-----------------
project-root/  
├── run_app.py            # Entry point to launch the GUI  
├── gui_app.py            # Tkinter interface and user workflows  
├── core_system.py        # Backend logic for patients, notes, and statistics  
├── support_utils.py      # Helpers: directories and date parsing  
├── auth_user.py          # Models authenticated user and permissions  
├── ward_department.py    # Department grouping for patients  
├── customer_patient.py   # Patient model holding visits & notes  
├── appointment_visit.py  # Visit data model  
├── clinical_note.py      # Clinical note data model  
├── data/                 # Input files (unchanged)  
│   ├── Credentials.csv  
│   ├── Patient_data.csv  
│   └── Notes.csv  
└── output/               # Created at runtime for logs and charts  

Prerequisites
-------------
- Python 3.8+  
- tkinter (bundled with Python)  
- matplotlib (`pip install matplotlib`)  

Installation
------------
1. Clone or download the repository.  
2. (Optional) Create and activate a virtual environment:  

python -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate.bat # Windows

3. Install dependencies:  
pip install matplotlib
Usage
-----
1. Ensure `data/` contains:
- Credentials.csv
- Patient_data.csv
- Notes.csv  

2. Run the application:

3. Login using a valid username/password from `Credentials.csv`.  
4. Select actions from the role-specific menu.  
5. Follow prompts to add/remove patients, retrieve records, count visits, view notes, or generate statistics.  
6. Logout or close the window to exit.  

Data Files
----------
- Credentials.csv  
Fixed-width concatenated entries: username + password (8 chars) + role (no headers).  
- Patient_data.csv  
CSV columns: Patient_ID, Visit_ID, Visittime, Visit_department, Gender, Race, Age, Ethnicity, Insurance, Zip_code, Chief_complaint  
- Notes.csv  
Fixed-width columns: PatientID(12) + VisitID(12) + NoteID(12) + Notetext(rest)  

UML Diagram
-----------
(See UML_Diagram.png in the repository for detailed class relationships.)  

Logging & Outputs
-----------------
- output/usage_log.csv  
Records: Username, Role, Action, Login Time, Action Time  
- output/visit_stats.png  
Bar chart of visits per day (all time or last N days)  

Contributing
------------
1. Fork the repo.  
2. Create a feature branch: `git checkout -b feature/YourFeature`  
3. Commit changes: `git commit -m "Add feature"`  
4. Push: `git push origin feature/YourFeature`  
5. Open a pull request.  

License
-------
MIT License. See LICENSE file for details.
