# TIC TAC TOE 

def print_board(board):
    """Displays the current game board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_winner(board):
    """Checks winner or if the game is a draw."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check for a draw
    if all(cell != " " for row in board for cell in row):
        return "Draw"

    return None


def play_game():
    """Main function to run the Tic Tac Toe game."""
    print("Welcome to Tic Tac Toe!")
    print("Player 1 is X and Player 2 is O")
    
    # Initializing the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Set the current player
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get valid move from the player
        while True:
            try:
                move = int(input(f"Enter your move (1-9): ")) - 1
                row, col = divmod(move, 3)
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Cell is already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter a number between 1 and 9.")

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "Draw":
                print("The game is a draw!")
            else:
                print(f"Player {winner} wins!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"



play_game()