import tkinter as tk
from tkinter import messagebox
from hms.services.auth_service import AuthService
from hms.utils.style import FONT_TITLE, FONT_NORMAL, PRIMARY_COLOR, WHITE, BG_COLOR

class LoginView(tk.Frame):
    def __init__(self, parent, on_login_success):
        super().__init__(parent, bg=BG_COLOR)
        self.on_login_success = on_login_success
        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self, text="Hospital Management System", font=FONT_TITLE, bg=BG_COLOR)
        title.pack(pady=(50, 20))

        # Login Frame
        login_frame = tk.Frame(self, bg=WHITE, padx=40, pady=40, relief=tk.RAISED, bd=2)
        login_frame.pack()

        # Username
        tk.Label(login_frame, text="Username:", font=FONT_NORMAL, bg=WHITE).grid(row=0, column=0, sticky='w', pady=10)
        self.username_entry = tk.Entry(login_frame, font=FONT_NORMAL, width=25)
        self.username_entry.grid(row=0, column=1, pady=10)

        # Password
        tk.Label(login_frame, text="Password:", font=FONT_NORMAL, bg=WHITE).grid(row=1, column=0, sticky='w', pady=10)
        self.password_entry = tk.Entry(login_frame, font=FONT_NORMAL, width=25, show="*")
        self.password_entry.grid(row=1, column=1, pady=10)

        # Login Button
        login_btn = tk.Button(login_frame, text="Login", font=FONT_NORMAL, bg=PRIMARY_COLOR, fg=WHITE, 
                              command=self.handle_login, width=15)
        login_btn.grid(row=2, column=0, columnspan=2, pady=(20, 0))

    def handle_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "Please enter both username and password")
            return

        try:
            user = AuthService.login(username, password)
            if user:
                self.on_login_success(user)
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to connect to database.\n{e}")
