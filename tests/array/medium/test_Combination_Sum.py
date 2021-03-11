from solutions.array.medium.Combination_Sum import Solution


def test():
    solution = Solution()
    assert solution.combinationSum([2, 3, 5], 8).__eq__(
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
    assert solution.combinationSum([2], 1).__eq__([])
    assert solution.combinationSum([1], 1).__eq__([[1]])
    assert solution.combinationSum([1], 2).__eq__([[1, 1]])
