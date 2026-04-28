import tkinter as tk
import sys
import os

# Add the parent directory to sys.path so 'hms' package is recognized
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hms.views.login_view import LoginView
from hms.views.dashboard_view import DashboardView
from hms.utils.style import set_theme

class HMSApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1024x768")
        set_theme(self.root)

        self.current_view = None
        self.show_login()

    def show_login(self):
        if self.current_view:
            self.current_view.destroy()
        
        self.current_view = LoginView(self.root, self.on_login_success)
        self.current_view.pack(fill=tk.BOTH, expand=True)

    def on_login_success(self, user):
        if self.current_view:
            self.current_view.destroy()
        
        self.current_view = DashboardView(self.root, user, self.on_logout)
        self.current_view.pack(fill=tk.BOTH, expand=True)

    def on_logout(self):
        self.show_login()

if __name__ == "__main__":
    root = tk.Tk()
    app = HMSApplication(root)
    root.mainloop()
