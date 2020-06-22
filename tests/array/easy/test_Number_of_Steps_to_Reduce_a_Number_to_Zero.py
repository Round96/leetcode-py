from solutions.array.easy.Number_of_Steps_to_Reduce_a_Number_to_Zero import Solution


def test():
    solution = Solution()
    assert solution.numberOfSteps(14) == 6
    assert solution.numberOfSteps(8) == 4
    assert solution.numberOfSteps(1024) == 11
