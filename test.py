
class ChessBoard:
    def __init__(self):
        # Initialize the board with pieces in their starting positions
        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],  # Black pieces
            ["p", "p", "p", "p", "p", "p", "p", "p"],  # Black pawns
            [" ", " ", " ", " ", " ", " ", " ", " "],  # Empty row
            [" ", " ", " ", " ", " ", " ", " ", " "],  # Empty row
            [" ", " ", " ", " ", " ", " ", " ", " "],  # Empty row
            [" ", " ", " ", " ", " ", " ", " ", " "],  # Empty row
            ["P", "P", "P", "P", "P", "P", "P", "P"],  # White pawns
            ["R", "N", "B", "Q", "K", "B", "N", "R"],  # White pieces
        ]
        self.turn = "white"  # White always goes first

    def print_board(self):
        # Print the board
        for row in self.board:
            print(" ".join(row))

    def is_valid_move(self, start, end):
        # Check if the move is within the board and follows the basic rules for pieces
        start_row, start_col = start
        end_row, end_col = end

        # Ensure both start and end positions are valid
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        start_piece = self.board[start_row][start_col]
        end_piece = self.board[end_row][end_col]

        # Check if the piece belongs to the correct player
        if (self.turn == "white" and start_piece.islower()) or (self.turn == "black" and start_piece.isupper()):
            return False  # Can't move opponent's pieces

        # Check if the destination is not occupied by the same color
        if (self.turn == "white" and end_piece.isupper()) or (self.turn == "black" and end_piece.islower()):
            return False

        # Simplified piece movement rules (only moving without checking exact legal moves)
        # You can expand these rules with specific piece movement logic.
        return True

    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end

        if self.is_valid_move(start, end):
            # Move the piece on the board
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = " "
            # Switch turn
            self.turn = "black" if self.turn == "white" else "white"
        else:
            print("Invalid move!")

# Game loop
def play_game():
    chess = ChessBoard()
    chess.print_board()

    while True:
        print(f"\n{chess.turn.capitalize()}'s turn:")
        start_pos = input("Enter the start position (e.g. e2): ").lower()
        end_pos = input("Enter the end position (e.g. e4): ").lower()

        # Convert positions from chess notation to board coordinates
        start_row, start_col = 8 - int(start_pos[1]), ord(start_pos[0]) - ord('a')
        end_row, end_col = 8 - int(end_pos[1]), ord(end_pos[0]) - ord('a')

        chess.move_piece((start_row, start_col), (end_row, end_col))
        chess.print_board()

# Start the game
play_game()