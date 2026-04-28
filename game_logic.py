class TicTacToeGame:
    """
    Handles the core game logic and board state for Tic Tac Toe.
    """
    def __init__(self):
        # The board is a list of 9 strings, initially empty spaces.
        self.board = [" " for _ in range(9)]
        self.current_winner = None
        self.winning_line = [] # Indices of the winning combination

    def available_moves(self):
        """Returns a list of indices that are empty on the board."""
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        """Checks if there are any empty squares left."""
        return " " in self.board

    def num_empty_squares(self):
        """Returns the number of empty squares."""
        return self.board.count(" ")

    def make_move(self, square, letter):
        """
        Attempts to place a letter on the given square.
        Returns True if successful, False otherwise.
        """
        if self.board[square] == " ":
            self.board[square] = letter
            # Check if this move resulted in a win
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        """Checks if the given letter has won the game after making a move at 'square'."""
        # 1. Check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            self.winning_line = [row_ind*3, row_ind*3 + 1, row_ind*3 + 2]
            return True
        
        # 2. Check the column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            self.winning_line = [col_ind, col_ind + 3, col_ind + 6]
            return True

        # 3. Check diagonals (only possible if the square is an even index: 0, 2, 4, 6, 8)
        if square % 2 == 0:
            diagonal1 = [self.board[0], self.board[4], self.board[8]] # Top-left to bottom-right
            if all([spot == letter for spot in diagonal1]):
                self.winning_line = [0, 4, 8]
                return True
            
            diagonal2 = [self.board[2], self.board[4], self.board[6]] # Top-right to bottom-left
            if all([spot == letter for spot in diagonal2]):
                self.winning_line = [2, 4, 6]
                return True
        
        return False
        
    def reset(self):
        """Resets the game state for a new round."""
        self.board = [" " for _ in range(9)]
        self.current_winner = None
        self.winning_line = []
