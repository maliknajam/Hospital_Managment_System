import tkinter as tk
from tkinter import ttk, messagebox
from hms.services.billing_service import BillingService
from hms.utils.style import FONT_HEADING, WHITE, BG_COLOR, PRIMARY_COLOR

class BillingView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG_COLOR)
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        tk.Label(self, text="Manage Billing", font=FONT_HEADING, bg=BG_COLOR).pack(pady=10)

        form_frame = tk.Frame(self, bg=WHITE, padx=20, pady=20)
        form_frame.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(form_frame, text="Patient ID:", bg=WHITE).grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.patient_id_entry = tk.Entry(form_frame)
        self.patient_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Amount ($):", bg=WHITE).grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self.amount_entry = tk.Entry(form_frame)
        self.amount_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Date:", bg=WHITE).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.date_entry = tk.Entry(form_frame)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Status:", bg=WHITE).grid(row=1, column=2, padx=5, pady=5, sticky='w')
        self.status_combo = ttk.Combobox(form_frame, values=["Unpaid", "Paid"], state="readonly")
        self.status_combo.set("Unpaid")
        self.status_combo.grid(row=1, column=3, padx=5, pady=5)

        btn_frame = tk.Frame(self, bg=BG_COLOR)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Add Bill", bg=PRIMARY_COLOR, fg=WHITE, command=self.add_bill).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_bill).pack(side=tk.LEFT, padx=10)

        columns = ("ID", "Patient", "Amount", "Status", "Date")
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        try:
            bills = BillingService.get_all_bills()
            for b in bills:
                self.tree.insert("", tk.END, values=(b['id'], b['patient_name'], f"${b['amount']}", b['status'], b['billing_date']))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_bill(self):
        p_id = self.patient_id_entry.get()
        amount = self.amount_entry.get()
        date = self.date_entry.get()
        status = self.status_combo.get()
        if not all([p_id, amount, date, status]):
            messagebox.showwarning("Warning", "All fields are required")
            return
        try:
            BillingService.add_bill(p_id, amount, status, date)
            self.load_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_bill(self):
        selected = self.tree.selection()
        if not selected:
            return
        bill_id = self.tree.item(selected[0])['values'][0]
        try:
            BillingService.delete_bill(bill_id)
            self.load_data()
        except Exception as e:
            messagebox.showerror("Error", str(e))
