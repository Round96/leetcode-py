from solutions.array.medium.Permutations import Solution


def test():
    solution = Solution()
    result = solution.permute([1, 2, 3])
    for arr in [[1, 2, 3], [1, 3, 2], [2, 1, 3],
                [2, 3, 1], [3, 1, 2], [3, 2, 1]]:
        assert arr in result
