from solutions.array.easy.Kids_With_the_Greatest_Number_of_Candies import Solution


def test():
    solution = Solution()
    assert solution.kidsWithCandies([2, 3, 5, 1, 3], 3).__eq__(
        [True, True, True, False, True])
