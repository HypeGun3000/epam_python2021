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
    list_o_ox = []
    list_o_oy = []
    list_x_ox = []
    list_x_oy = []
    list_x = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'x':
                list_x_ox.append(i)
                list_x_oy.append(j)


    print(list_x_ox, list_x_oy)


tic_tac_toe_checker([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]])
tic_tac_toe_checker([["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]])
