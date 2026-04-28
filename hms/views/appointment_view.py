import tkinter as tk
from tkinter import ttk, messagebox
from hms.services.appointment_service import AppointmentService
from hms.utils.style import FONT_HEADING, WHITE, BG_COLOR, PRIMARY_COLOR

class AppointmentView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG_COLOR)
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        tk.Label(self, text="Manage Appointments", font=FONT_HEADING, bg=BG_COLOR).pack(pady=10)

        form_frame = tk.Frame(self, bg=WHITE, padx=20, pady=20)
        form_frame.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(form_frame, text="Patient ID:", bg=WHITE).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.patient_id_entry = tk.Entry(form_frame)
        self.patient_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Doctor ID:", bg=WHITE).grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self.doctor_id_entry = tk.Entry(form_frame)
        self.doctor_id_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Date (YYYY-MM-DD):", bg=WHITE).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.date_entry = tk.Entry(form_frame)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Time (HH:MM):", bg=WHITE).grid(row=1, column=2, padx=5, pady=5, sticky='w')
        self.time_entry = tk.Entry(form_frame)
        self.time_entry.grid(row=1, column=3, padx=5, pady=5)

        btn_frame = tk.Frame(self, bg=BG_COLOR)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Add Appointment", bg=PRIMARY_COLOR, fg=WHITE, command=self.add_apt).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_apt).pack(side=tk.LEFT, padx=10)

        columns = ("ID", "Patient", "Doctor", "Date", "Time", "Status")
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        try:
            apts = AppointmentService.get_all_appointments()
            for a in apts:
                self.tree.insert("", tk.END, values=(a['id'], a['patient_name'], a['doctor_name'], a['appointment_date'], a['appointment_time'], a['status']))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_apt(self):
        p_id = self.patient_id_entry.get()
        d_id = self.doctor_id_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        if not all([p_id, d_id, date, time]):
            messagebox.showwarning("Warning", "All fields are required")
            return
        try:
            AppointmentService.add_appointment(p_id, d_id, date, time)
            self.load_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_apt(self):
        selected = self.tree.selection()
        if not selected:
            return
        apt_id = self.tree.item(selected[0])['values'][0]
        try:
            AppointmentService.delete_appointment(apt_id)
            self.load_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))
