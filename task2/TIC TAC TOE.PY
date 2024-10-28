import tkinter as tk
import math

# Constants for players
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# Check if the game is over
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    # Check for draw
    if all(cell != EMPTY for row in board for cell in row):
        return "Draw"
    
    return None

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    scores = {PLAYER_X: -1, PLAYER_O: 1, "Draw": 0}
    result = check_winner(board)
    
    if result is not None:
        return scores[result]

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(best_score, score)
        return best_score

# Get the best move for the AI
def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Update the board and check for winner
def make_move(row, col):
    if board[row][col] == EMPTY:
        board[row][col] = PLAYER_X
        buttons[row][col].config(text=PLAYER_X)
        
        result = check_winner(board)
        if result is not None:
            show_result(result)
            return
        
        # AI's turn
        row, col = best_move(board)
        if row != -1 and col != -1:
            board[row][col] = PLAYER_O
            buttons[row][col].config(text=PLAYER_O)

        result = check_winner(board)
        if result is not None:
            show_result(result)

# Show the result of the game
def show_result(result):
    if result == "Draw":
        message = "It's a draw!"
    else:
        message = f"The winner is: {result}"
    tk.messagebox.showinfo("Game Over", message)
    reset_board()

# Reset the game board
def reset_board():
    global board
    board = [[EMPTY] * 3 for _ in range(3)]
    for row in buttons:
        for button in row:
            button.config(text="")

# Create the main GUI window
def create_gui():
    global buttons, board
    buttons = []
    board = [[EMPTY] * 3 for _ in range(3)]

    root = tk.Tk()
    root.title("Tic Tac Toe")

    for i in range(3):
        row_buttons = []
        for j in range(3):
            button = tk.Button(root, text="", font=('Arial', 24), width=5, height=2,
                               command=lambda row=i, col=j: make_move(row, col))
            button.grid(row=i, column=j)
            row_buttons.append(button)
        buttons.append(row_buttons)

    reset_button = tk.Button(root, text="Reset", font=('Arial', 16), command=reset_board)
    reset_button.grid(row=3, column=0, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
