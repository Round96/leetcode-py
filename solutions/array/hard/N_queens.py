from typing import List, Tuple


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        for i in range(0, n):
            queens = self.generateInitialNQueens(n, 0, i)
            self.subSolveNQueens(0, i, queens, 1, n, result)

        return result

    def generateInitialNQueens(self, length: int, i, j):
        initialQueens = []
        for index in range(0, length):
            initialQueens.append([-1] * length)

        for indexI in range(0, i):
            for indexJ in range(0, length):
                initialQueens[indexI][indexJ] = 0

        for index in range(0, j):
            initialQueens[i][index] = 0

        return initialQueens

    def subSolveNQueens(
            self, i, j, queens: List[List[int]], queensNum: int, queensNeedNum: int, result: List[List[str]]):
        queens[i][j] = 1

        if queensNum == queensNeedNum:
            result.append(self.translateQueens(queens, queensNeedNum))
            return

        self.markAttchedQueens(i, j, queensNeedNum, queens)

        potentialQueenResult = self.findPotentialQueen(
            queensNeedNum, queens)

        for (potentialIndexI, potentialIndexJ) in potentialQueenResult:
            tempQueens = self.deepcopy(queens)

            self.subSolveNQueens(
                potentialIndexI,
                potentialIndexJ,
                tempQueens,
                queensNum + 1,
                queensNeedNum,
                result)

            queens[potentialIndexI][potentialIndexJ] = 0

    def markAttchedQueens(self, i, j, n: int, queens: List[List[int]]):
        for index in range(0, n):
            queens[i][index] = 0
            queens[index][j] = 0

            if i - index > -1 and j - index > -1:
                queens[i - index][j - index] = 0
            if i + index < n and j + index < n:
                queens[i + index][j + index] = 0

            if i - index > -1 and j + index < n:
                queens[i - index][j + index] = 0
            if i + index < n and j - index > -1:
                queens[i + index][j - index] = 0

        queens[i][j] = 1

    def findPotentialQueen(self, n: int, queens: List[List[int]]) -> Tuple:
        result = []
        for i in range(0, n):
            for j in range(0, n):
                if queens[i][j] == -1:
                    result.append((i, j))

        return result

    def translateQueens(
            self, queens: List[List[int]], n: int) -> List[List[str]]:
        result = []
        for i in range(0, n):
            str = ""
            for j in range(0, n):
                if queens[i][j] == 1:
                    str += "Q"
                else:
                    str += "."
            result.append(str)
        return result

    def deepcopy(self, queens):
        result = []
        for i in range(0, len(queens)):
            result.append(queens[i].copy())
        return result
