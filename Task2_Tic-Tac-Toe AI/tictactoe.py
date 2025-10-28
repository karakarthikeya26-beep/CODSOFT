
# Task 2: Tic-Tac-Toe AI using the Minimax Algorithm
# Author: Kara Karthikeya
# Project: CodSoft AI Internship

import math
import random



# Initialize the game board
board = [" " for _ in range(9)]

# Function to print the current board
def print_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()

# Check if a player has won
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Check if the board is full (draw)
def is_draw():
    return " " not in board

# Get a list of available moves (empty cells)
def available_moves():
    return [i for i in range(9) if board[i] == " "]

# Minimax algorithm implementation
def minimax(is_maximizing):
    # Base conditions
    if check_winner("O"):  # Computer wins
        return 1
    elif check_winner("X"):  # Human wins
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            board[move] = "O"
            score = minimax(False)
            board[move] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves():
            board[move] = "X"
            score = minimax(True)
            board[move] = " "
            best_score = min(best_score, score)
        return best_score

# Computer's best move using minimax
def computer_move():
    best_score = -math.inf
    best_move = None

    for move in available_moves():
        board[move] = "O"
        score = minimax(False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move

    board[best_move] = "O"

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X and the computer is O.")
    print_board()

    while True:
        # Player move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move not in range(9) or board[move] != " ":
                print("Invalid move! Please try again.")
                continue
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue

        board[move] = "X"
        print_board()

        if check_winner("X"):
            print("Congratulations! You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        print("Computer is making its move...")
        computer_move()
        print_board()

        if check_winner("O"):
            print("Computer wins! Better luck next time.")
            break
        if is_draw():
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
