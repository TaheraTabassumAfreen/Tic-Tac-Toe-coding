# Tic Tac Toe using Minimax (without Alpha-Beta Pruning)

import math

# Initial board
board = [' ' for _ in range(9)]

# Print board
def print_board():
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("---------")

# Check winner
def check_winner():
    win_combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a, b, c in win_combos:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    if ' ' not in board:
        return 'Draw'
    return None

# Minimax function
def minimax(is_maximizing):
    result = check_winner()
    if result == 'X':
        return 1
    elif result == 'O':
        return -1
    elif result == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Computer move
def computer_move():
    best_score = math.inf
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(True)
            board[i] = ' '
            if score < best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

# Game loop
while True:
    print_board()
    move = int(input("Enter your move (0-8): "))
    if board[move] != ' ':
        print("Invalid move!")
        continue

    board[move] = 'X'
    if check_winner():
        break

    computer_move()
    if check_winner():
        break

print_board()
winner = check_winner()
if winner == 'Draw':
    print("It's a Draw!")
else:
    print("Winner:", winner)
