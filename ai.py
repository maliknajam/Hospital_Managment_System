import math

class MinimaxAI:
    """
    Artificial Intelligence opponent using the Minimax algorithm.
    """
    def __init__(self, ai_letter="O", player_letter="X"):
        self.ai_letter = ai_letter
        self.player_letter = player_letter

    def get_best_move(self, game):
        """
        Finds the optimal move for the AI.
        """
        # Optimization: If it's the very first move of the game, taking the center
        # is always a strong opening and saves calculation time.
        if game.num_empty_squares() == 9:
            return 4 # Index 4 is the center square
            
        # Call the minimax algorithm to evaluate all possibilities
        return self.minimax(game, self.ai_letter)['position']

    def minimax(self, state, player):
        """
        Recursive Minimax algorithm.
        - Evaluates all possible futures to find the move that maximizes AI's score
          while minimizing the human's score.
        """
        max_player = self.ai_letter
        other_player = "O" if player == "X" else "X"

        # BASE CASE: Check if the previous move resulted in a win or draw
        if state.current_winner == other_player:
            # We multiply by num_empty_squares to prefer winning faster or losing slower
            score = 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
            return {'position': None, 'score': score}
        elif not state.empty_squares():
            return {'position': None, 'score': 0} # Draw has a score of 0

        # INITIALIZE BEST SCORE
        if player == max_player:
            best = {'position': None, 'score': -math.inf} # AI wants to maximize, so start very low
        else:
            best = {'position': None, 'score': math.inf}  # Human wants to minimize, so start very high

        # Explore all possible moves
        for possible_move in state.available_moves():
            # Step 1: Make a speculative move
            state.make_move(possible_move, player)
            
            # Step 2: Recursively call minimax to simulate the rest of the game after this move
            sim_score = self.minimax(state, other_player)
            
            # Step 3: Undo the move (backtrack)
            state.board[possible_move] = " "
            state.current_winner = None
            state.winning_line = []
            
            # Attach the move position to the score we got back
            sim_score['position'] = possible_move

            # Step 4: Update the best score dictionaries
            if player == max_player: # AI is trying to maximize
                if sim_score['score'] > best['score']:
                    best = sim_score
            else: # Human is trying to minimize
                if sim_score['score'] < best['score']:
                    best = sim_score
                    
        return best
