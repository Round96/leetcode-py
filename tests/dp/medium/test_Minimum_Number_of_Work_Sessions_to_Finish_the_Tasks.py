from solutions.dp.medium.Minimum_Number_of_Work_Sessions_to_Finish_the_Tasks import Solution


def test():
    solution = Solution()
    assert solution.minSessions(
        [1, 2, 2, 6, 3, 5, 5, 10, 4, 10, 1, 10, 3, 7], 13).__eq__(6)
