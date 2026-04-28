import tkinter as tk
from tkinter import ttk, messagebox
from hms.services.patient_service import PatientService
from hms.utils.style import FONT_HEADING, FONT_NORMAL, WHITE, BG_COLOR, PRIMARY_COLOR

class PatientView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG_COLOR)
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        # Header
        tk.Label(self, text="Manage Patients", font=FONT_HEADING, bg=BG_COLOR).pack(pady=10)

        # Form Frame
        form_frame = tk.Frame(self, bg=WHITE, padx=20, pady=20)
        form_frame.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(form_frame, text="Name:", bg=WHITE).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Age:", bg=WHITE).grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self.age_entry = tk.Entry(form_frame)
        self.age_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Gender:", bg=WHITE).grid(row=0, column=4, padx=5, pady=5, sticky='w')
        self.gender_combo = ttk.Combobox(form_frame, values=["Male", "Female", "Other"], state="readonly")
        self.gender_combo.grid(row=0, column=5, padx=5, pady=5)

        tk.Label(form_frame, text="Contact:", bg=WHITE).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.contact_entry = tk.Entry(form_frame)
        self.contact_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Address:", bg=WHITE).grid(row=1, column=2, padx=5, pady=5, sticky='w')
        self.address_entry = tk.Entry(form_frame)
        self.address_entry.grid(row=1, column=3, columnspan=3, sticky='we', padx=5, pady=5)

        # Buttons
        btn_frame = tk.Frame(self, bg=BG_COLOR)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Add Patient", bg=PRIMARY_COLOR, fg=WHITE, command=self.add_patient).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_patient).pack(side=tk.LEFT, padx=10)

        # Treeview (Table)
        columns = ("ID", "Name", "Age", "Gender", "Contact", "Address")
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        try:
            patients = PatientService.get_all_patients()
            for p in patients:
                self.tree.insert("", tk.END, values=(p.id, p.name, p.age, p.gender, p.contact_number, p.address))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_patient(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_combo.get()
        contact = self.contact_entry.get()
        address = self.address_entry.get()

        if not all([name, age, gender, contact, address]):
            messagebox.showwarning("Warning", "All fields are required")
            return
            
        try:
            PatientService.add_patient(name, age, gender, contact, address)
            messagebox.showinfo("Success", "Patient added successfully!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_patient(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a patient to delete")
            return
        
        patient_id = self.tree.item(selected[0])['values'][0]
        try:
            PatientService.delete_patient(patient_id)
            messagebox.showinfo("Success", "Patient deleted successfully!")
            self.load_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_combo.set('')
        self.contact_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
