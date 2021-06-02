from solutions.array.medium.Rotate_Image import Solution


def test():
    solution = Solution()
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution.rotate(matrix)
    assert matrix.__eq__([[15, 13, 2, 5], [14, 3, 4, 1],
                          [12, 6, 8, 9], [16, 7, 10, 11]])
