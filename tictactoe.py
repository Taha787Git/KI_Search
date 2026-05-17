"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == 0:
                o_count += 1
    if x_count <= o_count:
        return X
    else:
        return O
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for i in range (3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j)) 
    return moves
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #1 Board kopieren (wichtig!)
    new_board = copy.deepcopy(board)

    #2 Aktion entpacken
    i, j = action

    #3 Zug setzen
    new_board[i][j] = player(board)

    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
        # Reihen
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Spalten
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]

    # Diagonalen
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
        # 1. Gewinner prüfen
    if winner(board) is not None:
        return True

    # 2. Leere Felder prüfen
    for row in board:
        if EMPTY in row:
            return False

    # 3. sonst: Unentschieden
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def max_value(board, alpha, beta):
        if terminal(board):
            return utility(board)

        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action), alpha, beta))
            alpha = max(alpha, v)

            # ✂️ Pruning
            if alpha >= beta:
                break

        return v

    def min_value(board, alpha, beta):
        if terminal(board):
            return utility(board)

        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action), alpha, beta))
            beta = min(beta, v)

            # ✂️ Pruning
            if beta <= alpha:
                break

        return v

    # X (MAX)
    if player(board) == X:
        best_value = -math.inf
        best_move = None
        alpha = -math.inf
        beta = math.inf

        for action in actions(board):
            value = min_value(result(board, action), alpha, beta)
            if value > best_value:
                best_value = value
                best_move = action
            alpha = max(alpha, best_value)

        return best_move

    # O (MIN)
    else:
        best_value = math.inf
        best_move = None
        alpha = -math.inf
        beta = math.inf

        for action in actions(board):
            value = max_value(result(board, action), alpha, beta)
            if value < best_value:
                best_value = value
                best_move = action
            beta = min(beta, best_value)

        return best_move
    raise NotImplementedError
