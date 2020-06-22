from solutions.array.easy.Shuffle_the_Array import Solution


def test():
    solution = Solution()
    assert solution.shuffle([2, 5, 1, 3, 4, 7], 3).__eq__([2, 3, 5, 4, 1, 7])
    assert solution.shuffle([1, 2, 3, 4, 4, 3, 2, 1],
                            4).__eq__([1, 4, 2, 3, 3, 2, 4, 1])
