from solutions.array.medium.Spiral_Matrix2 import Solution


def test():
    solution = Solution()
    assert solution.generateMatrix(1).__eq__([[1]])
    assert solution.generateMatrix(2).__eq__([[1, 2], [4, 3]])
    assert solution.generateMatrix(3).__eq__([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
    assert solution.generateMatrix(4).__eq__(
        [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
    assert solution.generateMatrix(5).__eq__([[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [
        15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]])
