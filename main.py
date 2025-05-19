# main.py
# Entry point for the Patient Management System UI

import tkinter as tk
from ui_management import PatientManagementApp

def main():
    root = tk.Tk()
    app = PatientManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
