"""
gui_app.py - Tkinter interface for role-based patient management.
"""
import os, csv, datetime, tkinter as tk
from tkinter import simpledialog, messagebox
from support_utilis import ensure_dirs, parse_date
from auth_user import AuthUser
from core_system import HospitalSystem

class PatientManagementGUI:
    """Handles login screen and action menus."""
    def __init__(self, master):
        ensure_dirs()
        self.master = master
        self._load_creds()
        self.system = None
        self.user = None
        self._show_login()

    def _load_creds(self):
        """Read credentials.csv into a dict."""
        path = os.path.join('data','Credentials.csv')
        self.creds = {}
        with open(path, newline='', encoding='utf-8') as f:
            for row in csv.DictReader(f):
                u = row['username'].strip()
                self.creds[u] = (row['password'].strip(), row['role'].strip())

    def _show_login(self):
        """Display username/password fields."""
        self._clear()
        frm = tk.Frame(self.master, padx=20, pady=20)
        frm.pack()
        tk.Label(frm, text="Username:").grid(row=0,column=0)
        self.ent_user = tk.Entry(frm); self.ent_user.grid(row=0,column=1)
        tk.Label(frm, text="Password:").grid(row=1,column=0)
        self.ent_pwd = tk.Entry(frm, show="*"); self.ent_pwd.grid(row=1,column=1)
        tk.Button(frm, text="Login", command=self._do_login).grid(row=2,columnspan=2,pady=10)

    def _do_login(self):
        """Authenticate and show role-based menu."""
        u = self.ent_user.get().strip()
        p = self.ent_pwd.get().strip()
        cred = self.creds.get(u)
        if cred and cred[0]==p:
            self.user = AuthUser(u, cred[1], datetime.datetime.now())
            self.system = HospitalSystem(
                os.path.join('data','Patient_data.csv'),
                os.path.join('data','Notes.csv')
            )
            self._show_menu()
        else:
            messagebox.showerror("Error","Invalid credentials")

    def _show_menu(self):
        """Build buttons based on user.role."""
        self._clear()
        role = self.user.role
        frame = tk.Frame(self.master,padx=10,pady=10)
        frame.pack(side='left',fill='y')
        actions = []
        if role=='management':
            actions = [("Generate Stats",self._gen_stats),("Count Visits",self._count_visits),
                       ("Logout",self._show_login)]
        else:
            perms = self.user.permissions()
            mapping = {
                'add_patient': self._add_patient, 'remove_patient': self._remove_patient,
                'retrieve_patient': self._retrieve_patient, 'count_visits': self._count_visits,
                'view_note': self._view_note
            }
            for act,cmd in mapping.items():
                if act in perms:
                    actions.append((act.replace('_',' ').title(), cmd))
            actions.append(("Logout",self._show_login))

        for txt,cmd in actions:
            tk.Button(frame,text=txt,width=20,command=cmd).pack(pady=2)

        self.content = tk.Frame(self.master,padx=10,pady=10)
        self.content.pack(side='right',fill='both',expand=True)

    def _add_patient(self):
        pid = simpledialog.askstring("Add","Patient ID:")
        if not pid: return
        vt = simpledialog.askstring("Add","Visit date (YYYY-MM-DD):")
        if not parse_date(vt):
            messagebox.showerror("Error","Bad date")
            return
        dept = simpledialog.askstring("Add","Department:")
        gender = simpledialog.askstring("Add","Gender:")
        race = simpledialog.askstring("Add","Race:")
        age  = simpledialog.askinteger("Add","Age:")
        eth = simpledialog.askstring("Add","Ethnicity:")
        ins = simpledialog.askstring("Add","Insurance:")
        zipc= simpledialog.askstring("Add","Zip Code:")
        comp= simpledialog.askstring("Add","Chief Complaint:")
        self.system.add_visit(pid, vt, dept, gender, race, age, eth, ins, zipc, comp)
        self._show_message(f"Added visit for {pid}")

    def _remove_patient(self):
        pid = simpledialog.askstring("Remove","Patient ID:")
        self.system.remove_patient(pid or "")
        self._show_message(f"Removed {pid}")

    def _retrieve_patient(self):
        pid = simpledialog.askstring("Retrieve","Patient ID:")
        txt = self.system.retrieve_patient(pid or "")
        self._show_text(txt or "Not found")

    def _count_visits(self):
        ds = simpledialog.askstring("Count","Date (YYYY-MM-DD):")
        cnt = self.system.count_visits_on(ds or "")
        self._show_message(f"Visits on {ds}: {cnt}")

    def _view_note(self):
        pid = simpledialog.askstring("Note","Patient ID:")
        ds  = simpledialog.askstring("Note","Date (YYYY-MM-DD):")
        note=self.system.view_note(pid or "", ds or "")
        self._show_text(note or "No notes")

    def _gen_stats(self):
        days = simpledialog.askinteger("Stats","Last N days (0=all):")
        self.system.generate_statistics(days if days else None)
        self._show_message("Chart → output/visit_stats.png")

    def _show_message(self,msg):
        self._clear_content()
        tk.Label(self.content,text=msg,wraplength=400).pack()

    def _show_text(self,text):
        self._clear_content()
        box=tk.Text(self.content,wrap='word'); box.pack(fill='both',expand=True)
        box.insert('1.0',text); box.config(state='disabled')

    def _clear(self):
        for w in self.master.winfo_children(): w.destroy()

    def _clear_content(self):
        for w in self.content.winfo_children(): w.destroy()
