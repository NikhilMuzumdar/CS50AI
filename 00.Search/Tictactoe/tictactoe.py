"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
eval_count = 0 # Keep track of no of boards evaluated


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
    (Xcount, Ocount) = (0,0)
    for row in board:
        for element in row:
            if element == X:
                Xcount += 1
            elif element == O:
                Ocount += 1
    if Xcount > Ocount:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j] == EMPTY:
                possible_actions.append((i,j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    end_board = copy.deepcopy(board)
    end_board[action[0]][action[1]] = player(end_board)
    return end_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # A sub function to check and return winner in a 1D list
    def check_winner(l):
        (X_count, O_count) = (0,0)
        for element in l:
            if element == X:
                X_count += 1
            elif element == O:
                O_count += 1
        if X_count == len(l):
            return X
        elif O_count == len(l):
            return O

    # Check all possible combinations of win
    combinations = []
    for i in range(len(board)):
        combinations.append(board[i]) # Iterate over rows and append them
        combinations.append([board[col][i] for col in range(len(board)) ]) # Iterate over columns and append them
    # Add diagonals
    combinations.append([board[i][i] for i in range(len(board))]) # Diagonal 1
    combinations.append([board[i][len(board)-i-1] for i in range(len(board))]) # Diagonal 2

    for element in combinations:
        if check_winner(element) == X:
            return X
        elif check_winner(element) == O:
            return O

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in [X,O]:
        return True
    # Check if there are no moves left
    elif len(actions(board)) == 0:
            return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    else:
        if player(board) == X:
            return max_value(board)[-1]
        else:
            return min_value(board)[-1]


def max_value(board):
    """Returns a move for given board state with max of minimum values"""
    print_board(board)
    if terminal(board):
        return utility(board), None

    value = float('-inf')
    next_action = None
    for action in actions(board):
        temp_value, temp_action = min_value(result(board, action))
        if temp_value > value:
            value, next_action = temp_value, action
            if value == 1:
                return value, next_action
    return value, next_action

def min_value(board):
    """Returns a move for given board state with max of minimum values"""
    print_board(board)
    if terminal(board):
        return utility(board), None

    value = float('inf')
    next_action = None
    for action in actions(board):
        temp_value, temp_action = max_value(result(board, action))
        if temp_value < value:
            value, next_action = temp_value, action
            if value == -1:
                return value, next_action
    return value, next_action

def print_board(board):
    """A func to print all the boards evaluated with total count thus far"""
    global eval_count
    eval_count += 1
    print(f'# {eval_count} boards evaluated!')
    print_board = copy.deepcopy(board)
    for row in print_board:
        for indx in range(len(row)):
            if row[indx] == None:
                row[indx] = '_'
        print(row)
    print()