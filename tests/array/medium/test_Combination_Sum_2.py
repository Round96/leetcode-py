from solutions.array.medium.Combination_Sum_2 import Solution


def test():
    solution = Solution()
    assert solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8).__eq__(
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
    assert solution.combinationSum2(
        [2, 5, 2, 1, 2], 5).__eq__([[1, 2, 2], [5]])
    assert solution.combinationSum2(
        [3, 1, 3, 5, 1, 1], 8).__eq__([[1, 1, 1, 5], [1, 1, 3, 3], [3, 5]])
