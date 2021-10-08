"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    if tic_tac_toe_horizontal(board):
        return f'{tic_tac_toe_horizontal(board)} wins!'
    elif tic_tac_toe_vertical(board):
        return f'{tic_tac_toe_vertical(board)} wins!'
    elif tic_tac_toe_same_indexes(board):
        return f'{tic_tac_toe_same_indexes(board)} wins!'
    elif tic_tac_toe_draw(board):
        return 'draw!'
    else:
        return 'unfinished'


def tic_tac_toe_horizontal(board: List[List]) -> str:
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]


def tic_tac_toe_vertical(board: List[List]) -> str:
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]


def tic_tac_toe_same_indexes(board: List[List]) -> str:
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]


def tic_tac_toe_draw(board: List[List]) -> str:
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '-':
                return "draw!"
