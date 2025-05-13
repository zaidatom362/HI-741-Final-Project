"""
core_system.py - Backend for patients, visits, notes, stats.
"""
import csv, os
import matplotlib.pyplot as plt
from collections import defaultdict
from ward_department import WardDepartment
from customer_patient import CustomerPatient
from appointment_visit import AppointmentVisit
from clinical_note import ClinicalNote
from support_utilis import parse_date

class HospitalSystem:
    """Loads data, provides CRUD and stats."""
    def __init__(self, pat_path, note_path):
        self.patients = {}
        self.departments = {}
        self._load_patients(pat_path)
        self._load_notes(note_path)

    def _load_patients(self,path):
        try:
            with open(path,newline='',encoding='utf-8') as f:
                for r in csv.DictReader(f):
                    pid = r['Patient_ID'].strip()
                    if pid not in self.patients:
                        self.patients[pid] = CustomerPatient(pid)
                    dept = r['Visit_department'].strip()
                    if dept not in self.departments:
                        self.departments[dept] = WardDepartment(dept)
                    dt = parse_date(r['Visit_time'].strip())
                    visit = AppointmentVisit(
                        r['Visit_ID'].strip(), dt,
                        self.departments[dept],
                        r['Gender'].strip(), r['Race'].strip(),
                        int(r['Age']), r['Ethnicity'].strip(),
                        r['Insurance'].strip(), r['Zip_code'].strip(),
                        r['Chief_complaint'].strip()
                    )
                    self.patients[pid].add_visit(visit)
                    self.departments[dept].add_patient(self.patients[pid])
        except FileNotFoundError:
            print("Patient data missing.")

    def _load_notes(self,path):
        try:
            with open(path,newline='',encoding='utf-8',errors='replace') as f:
                for r in csv.DictReader(f):
                    pid = r['Patient_ID'].strip()
                    if pid in self.patients:
                        note = ClinicalNote(
                            r['Note_ID'].strip(),
                            r['Visit_ID'].strip(),
                            r['Note_text'].strip()
                        )
                        self.patients[pid].add_note(note)
        except FileNotFoundError:
            print("Notes missing.")

    def add_visit(self, pid, vt, dept, gender, race, age, eth, ins, zipc, comp):
        if pid not in self.patients:
            self.patients[pid] = CustomerPatient(pid)
        if dept not in self.departments:
            self.departments[dept] = WardDepartment(dept)
        visit = AppointmentVisit(
            str(os.urandom(4).hex()), vt,
            self.departments[dept], gender, race, age, eth, ins, zipc, comp
        )
        self.patients[pid].add_visit(visit)
        self.departments[dept].add_patient(self.patients[pid])
        # append to CSV
        with open(os.path.join('data','Patient_data.csv'),'a',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(vars(visit).keys()))
            w.writerow(vars(visit))

    def remove_patient(self, pid):
        self.patients.pop(pid, None)
        rows=[]
        path=os.path.join('data','Patient_data.csv')
        with open(path,newline='',encoding='utf-8') as f:
            rows = [r for r in csv.DictReader(f) if r['Patient_ID']!=pid]
        with open(path,'w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=rows[0].keys() if rows else [])
            w.writeheader(); w.writerows(rows)

    def retrieve_patient(self, pid):
        if pid not in self.patients: return None
        p = self.patients[pid]
        return "\n".join(f"{note.id}: {note.text}" for note in p.notes) \
            if not p.visits else \
            "\n".join(str(vars(v)) for v in p.visits)

    def view_note(self, pid, ds):
        if pid not in self.patients: return None
        return "\n\n".join(n.text for n in self.patients[pid].notes
                           if str(n.visit_id).startswith(ds))

    def count_visits_on(self, ds):
        return sum(1 for p in self.patients.values()
                   for v in p.visits
                   if str(v.time).startswith(ds))

    def generate_statistics(self, days=None):
        counts=defaultdict(int)
        for p in self.patients.values():
            for v in p.visits:
                d=str(v.time)[:10]; counts[d]+=1
        if days:
            cutoff=datetime.datetime.now()-datetime.timedelta(days=days)
            counts={d:c for d,c in counts.items()
                    if datetime.datetime.strptime(d,"%Y-%m-%d")>=cutoff}
        dates=sorted(counts); vals=[counts[d] for d in dates]
        os.makedirs('output',exist_ok=True)
        plt.bar(dates,vals); plt.xticks(rotation=45); plt.tight_layout()
        plt.savefig('output/visit_stats.png'); plt.close()
