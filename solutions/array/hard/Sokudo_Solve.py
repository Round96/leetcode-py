# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
from typing import List

str_array = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        (x, y) = self.findUnassigned(board)
        if (x, y) == (-1, -1):
            return

        for num in str_array:
            board[x][y] = num
            if self.isNumValid(x, y, board):
                self.solveSudoku(board)
                if self.isBoardFullFilled(board):
                    return
            board[x][y] = "."

    def isBoardFullFilled(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    return False
        return True

    def findUnassigned(self, board: List[List[str]]):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    return (i, j)
        return (-1, -1)

    def isNumValid(self, i, j, board: List[List[str]]) -> bool:
        num = board[i][j]

        # row check
        for index in range(0, 9):
            if num == board[i][index] and j != index:
                return False

        # column check
        for index in range(0, 9):
            if num == board[index][j] and i != index:
                return False

        # grid check
        top_left_x_index = 3 * int(i / 3)
        top_left_y_index = 3 * int(j / 3)
        for index in range(0, 9):
            temp_x = top_left_x_index + int(index / 3)
            temp_y = top_left_y_index + index % 3
            if num == board[temp_x][temp_y] and temp_x != i and temp_y != j:
                return False

        return True
