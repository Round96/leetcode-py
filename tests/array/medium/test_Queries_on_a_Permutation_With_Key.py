from solutions.array.medium.Queries_on_a_Permutation_With_Key import Solution


def test():
    solution = Solution()
    assert solution.processQueries([3, 1, 2, 1], 5).__eq__([2, 1, 2, 1])
    assert solution.processQueries([4, 1, 2, 2], 4).__eq__([3, 1, 2, 0])
    assert solution.processQueries([7, 5, 5, 8, 3], 8).__eq__([6, 5, 0, 7, 5])
