import tkinter as tk
from tkinter import ttk
from hms.utils.style import FONT_HEADING, FONT_TITLE, WHITE, BG_COLOR, PRIMARY_COLOR
from hms.views.patient_view import PatientView
from hms.views.doctor_view import DoctorView
from hms.views.appointment_view import AppointmentView
from hms.views.medical_record_view import MedicalRecordView
from hms.views.billing_view import BillingView

class DashboardView(tk.Frame):
    def __init__(self, parent, user, on_logout):
        super().__init__(parent, bg=BG_COLOR)
        self.user = user
        self.on_logout = on_logout
        self.create_widgets()

    def create_widgets(self):
        # Top Navigation Bar
        nav_bar = tk.Frame(self, bg=PRIMARY_COLOR, height=50)
        nav_bar.pack(fill=tk.X, side=tk.TOP)

        tk.Label(nav_bar, text=f"HMS Dashboard - Welcome, {self.user.username} ({self.user.role})", 
                 bg=PRIMARY_COLOR, fg=WHITE, font=FONT_HEADING).pack(side=tk.LEFT, padx=20, pady=10)
        
        tk.Button(nav_bar, text="Logout", command=self.on_logout).pack(side=tk.RIGHT, padx=20, pady=10)

        # Notebook for Tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Tabs
        self.patient_tab = PatientView(self.notebook)
        self.notebook.add(self.patient_tab, text="Patients")

        self.doctor_tab = DoctorView(self.notebook)
        self.notebook.add(self.doctor_tab, text="Doctors")

        self.appointment_tab = AppointmentView(self.notebook)
        self.notebook.add(self.appointment_tab, text="Appointments")

        self.medical_record_tab = MedicalRecordView(self.notebook)
        self.notebook.add(self.medical_record_tab, text="Medical Records")

        self.billing_tab = BillingView(self.notebook)
        self.notebook.add(self.billing_tab, text="Billing")
