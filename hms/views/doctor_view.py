import tkinter as tk
from tkinter import ttk, messagebox
from hms.services.doctor_service import DoctorService
from hms.utils.style import FONT_HEADING, WHITE, BG_COLOR, PRIMARY_COLOR

class DoctorView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG_COLOR)
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        tk.Label(self, text="Manage Doctors", font=FONT_HEADING, bg=BG_COLOR).pack(pady=10)

        form_frame = tk.Frame(self, bg=WHITE, padx=20, pady=20)
        form_frame.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(form_frame, text="Name:", bg=WHITE).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Specialty:", bg=WHITE).grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self.specialty_entry = tk.Entry(form_frame)
        self.specialty_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Contact:", bg=WHITE).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.contact_entry = tk.Entry(form_frame)
        self.contact_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Availability:", bg=WHITE).grid(row=1, column=2, padx=5, pady=5, sticky='w')
        self.avail_entry = tk.Entry(form_frame)
        self.avail_entry.grid(row=1, column=3, padx=5, pady=5)

        btn_frame = tk.Frame(self, bg=BG_COLOR)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Add Doctor", bg=PRIMARY_COLOR, fg=WHITE, command=self.add_doctor).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_doctor).pack(side=tk.LEFT, padx=10)

        columns = ("ID", "Name", "Specialty", "Contact", "Availability")
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        try:
            doctors = DoctorService.get_all_doctors()
            for d in doctors:
                self.tree.insert("", tk.END, values=(d.id, d.name, d.specialty, d.contact_number, d.availability))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_doctor(self):
        name = self.name_entry.get()
        spec = self.specialty_entry.get()
        cont = self.contact_entry.get()
        avail = self.avail_entry.get()
        if not all([name, spec, cont, avail]):
            messagebox.showwarning("Warning", "All fields are required")
            return
        try:
            DoctorService.add_doctor(name, spec, cont, avail)
            self.load_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_doctor(self):
        selected = self.tree.selection()
        if not selected:
            return
        doctor_id = self.tree.item(selected[0])['values'][0]
        try:
            DoctorService.delete_doctor(doctor_id)
            self.load_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))
