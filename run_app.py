"""
Entry point: Launches the Tkinter GUI.
"""
import tkinter as tk
from gui_app import PatientManagementGUI

def main():
    root = tk.Tk()
    root.title("Hospital Management System")
    app = PatientManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
