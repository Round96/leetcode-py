from solutions.array.hard.First_Missing_Positive import Solution


def test():
    solution = Solution()
    assert solution.firstMissingPositive([1, 2, 0]).__eq__(3)
    assert solution.firstMissingPositive([3, 4, -1, 1]).__eq__(2)
    assert solution.firstMissingPositive([7, 8, 9, 11, 12]).__eq__(1)
    assert solution.firstMissingPositive([2, 1]).__eq__(3)
    assert solution.firstMissingPositive([1, 2, 6, 3, 5, 4]).__eq__(7)
    assert solution.firstMissingPositive([0, 2, 2, 1, 1]).__eq__(3)
    assert solution.firstMissingPositive([0, 3, 4, 2, 2, 1, 1, 3, 4]).__eq__(5)
