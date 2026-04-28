import tkinter as tk
from game_logic import TicTacToeGame
from ai import MinimaxAI

class TicTacToeGUI:
    """
    Graphical User Interface for the Tic Tac Toe game.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe vs AI")
        self.root.configure(bg="#2E3440") # Dark theme background
        
        # Initialize Game and AI instances
        self.game = TicTacToeGame()
        self.ai = MinimaxAI(ai_letter="O", player_letter="X")
        
        self.human_turn = True # Human is X, AI is O. Human goes first.
        
        # UI Elements
        self.buttons = []
        self.create_widgets()
        
    def create_widgets(self):
        # Header Label to indicate turns
        self.turn_label = tk.Label(
            self.root, text="Your Turn (X)", font=("Helvetica", 16, "bold"), 
            bg="#2E3440", fg="#D8DEE9"
        )
        self.turn_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Game Board Frame
        board_frame = tk.Frame(self.root, bg="#4C566A")
        board_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=10)
        
        # 3x3 Grid Buttons
        for i in range(9):
            btn = tk.Button(
                board_frame, text=" ", font=("Helvetica", 32, "bold"),
                width=3, height=1, bg="#3B4252", fg="#E5E9F0",
                activebackground="#4C566A", activeforeground="#E5E9F0",
                command=lambda i=i: self.on_button_click(i)
            )
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)
            
        # Restart Button
        restart_btn = tk.Button(
            self.root, text="Restart Game", font=("Helvetica", 12, "bold"),
            bg="#81A1C1", fg="#2E3440", activebackground="#5E81AC",
            command=self.reset_game
        )
        restart_btn.grid(row=2, column=0, columnspan=3, pady=15)
        
    def on_button_click(self, index):
        """Triggered when a human player clicks a spot on the board."""
        # Only allow click if it's human's turn and the spot is empty
        if self.human_turn and self.game.board[index] == " ":
            # Make Human Move
            self.make_move(index, "X")
            
            # Check if game is still ongoing
            if not self.game.current_winner and self.game.empty_squares():
                self.human_turn = False
                self.turn_label.config(text="AI's Turn (O)", fg="#EBCB8B")
                self.root.update() # Force UI to update before AI calculates
                
                # Schedule AI move slightly delayed for better user experience
                self.root.after(300, self.ai_move)

    def ai_move(self):
        """Calculates and makes the AI's move."""
        best_square = self.ai.get_best_move(self.game)
        
        if best_square is not None:
            self.make_move(best_square, "O")
            
            # Check if game is still ongoing
            if not self.game.current_winner and self.game.empty_squares():
                self.human_turn = True
                self.turn_label.config(text="Your Turn (X)", fg="#D8DEE9")

    def make_move(self, index, letter):
        """Executes a move and updates the UI."""
        if self.game.make_move(index, letter):
            # Update Button Text and Color
            btn = self.buttons[index]
            btn.config(text=letter)
            
            if letter == "X":
                btn.config(fg="#88C0D0") # Cyan color for X
            else:
                btn.config(fg="#BF616A") # Red color for O
                
            # Check for win or draw to end the game
            if self.game.current_winner:
                self.highlight_winner()
                self.end_game(f"{'You win' if letter == 'X' else 'AI wins'}!")
            elif not self.game.empty_squares():
                self.end_game("It's a Draw!")
                
    def highlight_winner(self):
        """Highlights the winning combination on the board."""
        for index in self.game.winning_line:
            self.buttons[index].config(bg="#A3BE8C", fg="#2E3440") # Green background
            
    def end_game(self, message):
        """Ends the game, displays result, and disables buttons."""
        color = "#A3BE8C" if "win" in message and "You" in message else "#BF616A" if "AI" in message else "#EBCB8B"
        self.turn_label.config(text=message, fg=color)
        
        # Disable all buttons to prevent further play until restart
        for btn in self.buttons:
            btn.config(state="disabled")
            
    def reset_game(self):
        """Resets the game state and UI to start a new game."""
        self.game.reset()
        self.human_turn = True
        self.turn_label.config(text="Your Turn (X)", fg="#D8DEE9")
        
        for btn in self.buttons:
            btn.config(
                text=" ", state="normal",
                bg="#3B4252", fg="#E5E9F0"
            )
