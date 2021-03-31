from solutions.array.hard.Trapping_rain_water import Solution


def test():
    solution = Solution()
    assert solution.trap([]).__eq__(0)
    assert solution.trap([2, 0, 2]).__eq__(2)
    assert solution.trap([4, 2, 0, 3, 2, 5]).__eq__(9)
    assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]).__eq__(6)
