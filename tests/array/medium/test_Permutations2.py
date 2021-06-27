from solutions.array.medium.Permutations2 import Solution


def test():
    solution = Solution()
    result = solution.permuteUnique([1, 2, 3])
    for arr in [[1, 2, 3], [1, 3, 2], [2, 1, 3],
                [2, 3, 1], [3, 1, 2], [3, 2, 1]]:
        assert arr in result
    assert len(result) == 6

    result = solution.permuteUnique([1, 1, 2])
    for arr in [[1, 1, 2],
                [1, 2, 1],
                [2, 1, 1]]:
        assert arr in result
    assert len(result) == 3
