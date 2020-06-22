from solutions.array.easy.How_Many_Numbers_Are_Smaller_Than_the_Current_Number import Solution


def test():
    solution = Solution()
    assert solution.smallerNumbersThanCurrent(
        [8, 1, 2, 2, 3]).__eq__([4, 0, 1, 1, 3])
