from typing import List
import logging

logger = logging.getLogger()


# No need to add comments
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isRowValid(board) and self.isColumnValid(
            board) and self.isEachGridValid(board)

    def isRowValid(self, board: List[List[str]]) -> bool:
        for row in board:
            occurred_numbers = {}
            for num in row:
                if num != ".":
                    if num in occurred_numbers:
                        return False
                    else:
                        occurred_numbers[num] = 0
        return True

    def isColumnValid(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            occurred_numbers = {}
            for j in range(0, 9):
                if board[j][i] != ".":
                    if board[j][i] in occurred_numbers:
                        return False
                    else:
                        occurred_numbers[board[j][i]] = 0
        return True

    def isEachGridValid(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            occurred_numbers = {}
            for j in range(0, 9):
                num = board[3 * int(i / 3) + int(j / 3)][3 * (i % 3) + j %
                                                         3]
                if num != ".":
                    if num in occurred_numbers:
                        logger.info(i)
                        logger.info(j)
                        logger.info(num)
                        logger.info(3)
                        return False
                    else:
                        occurred_numbers[num] = 0
        return True
