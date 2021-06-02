from solutions.array.medium.Jump_Game2 import Solution


def test():
    solution = Solution()
    assert solution.jump([3, 2, 1]).__eq__(1)
    assert solution.jump([2, 3, 1]).__eq__(1)
    assert solution.jump([2, 3, 1, 1, 4]).__eq__(2)
    assert solution.jump([2, 3, 0, 1, 4]).__eq__(2)
    assert solution.jump([2, 3, 0, 1, 4, 1, 2, 4]).__eq__(3)
    assert solution.jump([1, 2, 3, 4, 5]).__eq__(3)
    assert solution.jump([3, 4, 3, 2, 5, 4, 3]).__eq__(3)
    assert solution.jump([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]).__eq__(2)
