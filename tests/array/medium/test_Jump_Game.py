from solutions.array.medium.Jump_Game import Solution


def test():
    solution = Solution()
    assert solution.canJump([0]).__eq__(True)
    assert solution.canJump([3, 2, 1]).__eq__(True)
    assert solution.canJump([2, 3, 1]).__eq__(True)
    assert solution.canJump([2, 3, 1, 1, 4]).__eq__(True)
    assert solution.canJump([3, 2, 1, 0, 4]).__eq__(False)
    assert solution.canJump([1, 1, 0, 1]).__eq__(False)
