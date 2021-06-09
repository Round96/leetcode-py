from solutions.array.medium.Spiral_Matrix import Solution


def test():
    solution = Solution()
    assert solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).__eq__([
        1, 2, 3, 6, 9, 8, 7, 4, 5])
    assert solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]).__eq__(
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    assert solution.spiralOrder([[7], [9], [6]]).__eq__([7, 9, 6])
    assert solution.spiralOrder(
        [[2, 5, 8], [4, 0, -1]]).__eq__([2, 5, 8, -1, 0, 4])
    assert solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [
                                13, 14, 15, 16]]).__eq__([1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])
    assert solution.spiralOrder(
        [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]).__eq__([2, 3, 4, 7, 10, 13, 16, 15, 14, 11, 8, 5, 6, 9, 12])
    assert solution.spiralOrder(
        [[2, 5], [8, 4], [0, -1]]).__eq__([2, 5, 4, -1, 0, 8])
