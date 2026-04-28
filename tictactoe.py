import tkinter as tk
from gui import TicTacToeGUI

def main():
    """
    Main entry point for the Tic Tac Toe application.
    """
    root = tk.Tk()
    
    # Set a fixed window size for consistent appearance
    root.geometry("350x450")
    root.resizable(False, False)
    
    # Initialize the GUI application
    app = TicTacToeGUI(root)
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
