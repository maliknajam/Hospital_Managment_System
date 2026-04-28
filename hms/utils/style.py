# Colors
BG_COLOR = "#87CEEB"
PRIMARY_COLOR = "#007bff"
SECONDARY_COLOR = "#6c757d"
TEXT_COLOR = "#333333"
WHITE = "#ffffff"
SUCCESS_COLOR = "#28a745"
DANGER_COLOR = "#dc3545"

# Fonts
FONT_TITLE = ("Helvetica", 24, "bold")
FONT_HEADING = ("Helvetica", 16, "bold")
FONT_NORMAL = ("Helvetica", 12)
FONT_SMALL = ("Helvetica", 10)

def set_theme(root):
    """Applies a consistent theme to the Tkinter root window."""
    root.configure(bg=BG_COLOR)
