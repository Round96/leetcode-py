from solutions.array.hard.N_queens import Solution


def test():
    solution = Solution()
    assert solution.solveNQueens(1).__eq__([["Q"]])
    assert solution.solveNQueens(4).__eq__(
        [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
    assert solution.solveNQueens(5).__eq__(
        [["Q....", "..Q..", "....Q", ".Q...", "...Q."],
         ["Q....", "...Q.", ".Q...", "....Q", "..Q.."],
         [".Q...", "...Q.", "Q....", "..Q..", "....Q"],
         [".Q...", "....Q", "..Q..", "Q....", "...Q."],
         ["..Q..", "Q....", "...Q.", ".Q...", "....Q"],
         ["..Q..", "....Q", ".Q...", "...Q.", "Q...."],
         ["...Q.", "Q....", "..Q..", "....Q", ".Q..."],
         ["...Q.", ".Q...", "....Q", "..Q..", "Q...."],
         ["....Q", ".Q...", "...Q.", "Q....", "..Q.."],
         ["....Q", "..Q..", "Q....", "...Q.", ".Q..."]])
