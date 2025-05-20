🏥 Hospital Clinical Data Warehouse

Welcome! This project is a user-friendly hospital management system built with Python and Tkinter. It streamlines patient visit tracking, clinical notes, and hospital statistics, all while keeping data secure and access role-based.
🚀 What Does This App Do?

Role-based login: Only see what you’re allowed to see.

Clinician/Nurse: Add, remove, and retrieve patients, view clinical notes, and count visits.

Admin: Count visits and (optionally) generate statistics.

Management: Generate hospital statistics.

Everything happens in a modern, simple GUI. No terminal commands needed after launch.

🗂️ Project Structure

```
project-root/
├── src/
│   ├── main.py
│   ├── department.py
│   ├── note.py
│   ├── patient.py
│   ├── patient_management.py
│   ├── ui_management.py
│   ├── user.py
│   ├── utils.py
│   ├── visit.py
├── data/
│   ├── Credentials.csv
│   ├── Patient_data.csv
│   ├── Notes.csv
├── output/
│   ├── usage_log.csv
│   ├── visit_stats.png
│   ├── output.txt
├── UML_Diagram.png
├── README.md
```
🏃‍♂️ How to Run

Install requirements:

```pip install matplotlib```

Go to the code folder:

```cd src```

Start the app

```python main.py```

Login using a username and password from ../data/Credentials.csv.

Please enter the date when asked for, in the exact date format the prompt asks you (e.g., YYYY-MM-DD).If you use the wrong format, you may get an error or no results.

👤 User Roles & Permissions
Role	What They Can Do
admin	Count Visits, (optionally) Generate Statistics
clinician	Add/Remove/Retrieve Patient, View Note, Count Visits
nurse	Add/Remove/Retrieve Patient, View Note, Count Visits
management	Generate Statistics
📑 Data & Outputs
```
data/Credentials.csv: Usernames, passwords, and roles.

data/Patient_data.csv: All patient and visit info.

data/Notes.csv: Clinical notes.

output/usage_log.csv: Who did what and when.

output/visit_stats.png: Hospital visit statistics chart.

output/output.txt: Patient info export.
```
🖼️ UML Diagram

See UML_Diagram.png for a visual map of all classes and their relationships.

Key connections:

The system manages patients and departments.

Patients have visits and notes.

Visits are linked to departments.

Notes are linked to visits.

🛠️ Troubleshooting

KeyError? Double-check your CSV column names (like Zip_code) match exactly.

Login not working? Make sure your username and password are in Credentials.csv.

GUI won’t start? Make sure you’re running python main.py from inside src/ and have installed all requirements.

Date errors? Always enter the date exactly as the prompt specifies (usually YYYY-MM-DD).

📬 Questions?

If you get stuck, check the logs in output/usage_log.csv or contact me.
📝 License

MIT License. See LICENSE for details.
