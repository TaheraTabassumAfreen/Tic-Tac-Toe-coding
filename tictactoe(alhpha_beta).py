import math

def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print("--+---+--")

def check_winner(board):
    win_conditons = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    for a,b,c in win_conditons:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None
    
def is_draw(board):
    return " " not in board

def minimax(board, is_maximizing, counter):
    counter[0] += 1
    winner = check_winner(board)

    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if is_draw(board):
        return 0 
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False, counter)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True, counter)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score
    
def alphabeta(board, is_maximizing, alpha, beta, counter):
    counter[0] += 1
    winner = check_winner(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if is_draw(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = alphabeta(board, False, alpha, beta, counter)
                board[i] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = alphabeta(board, True, alpha, beta, counter)
                board[i] = " "
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score
    
def best_move(board):
    
    minimax_counter = [0]
    alphabeta_counter = [0]

    
    _ = minimax(board, True, minimax_counter)

    
    _ = alphabeta(board, True, -math.inf, math.inf, alphabeta_counter)

    
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = alphabeta(board, False, -math.inf, math.inf, [0])
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i

    print(f"Nodes explored - Minimax: {minimax_counter[0]}, Alpha-Beta: {alphabeta_counter[0]}")
    return move

def tic_tac_toe():
    board = [" "] * 9

    print("You are X, AI is O")
    print("Positions:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

    while True:
        print_board(board)

        move = int(input("Your Move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalide move!")
            continue
        board[move] = "X"

        if check_winner(board) == "X":
            print_board(board)
            print("You WINS.")
            break

        if is_draw(board):
            print_board(board)
            print("S It's a DRAW")
            break

        ai_move = best_move(board)
        board[ai_move] = "O"

        if check_winner(board) == "O":
            print_board(board)
            print("AI WINS.")
            break

        if is_draw(board):
            print_board(board)
            print("It's a DRAW")
            break

tic_tac_toe()