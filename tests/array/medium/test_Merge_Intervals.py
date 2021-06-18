from solutions.array.medium.Merge_Intervals import Solution


def test():
    solution = Solution()
    assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]).__eq__(
        [[1, 6], [8, 10], [15, 18]])
    assert solution.merge([[1, 3], [3, 6]]).__eq__([[1, 6]])
    assert solution.merge([[1, 4], [0, 4]]).__eq__([[0, 4]])
    assert solution.merge([[1, 4], [2, 8], [1, 9]]).__eq__([[1, 9]])
