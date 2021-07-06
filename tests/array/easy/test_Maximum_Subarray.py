from solutions.array.easy.Maximum_Subarray import Solution


def test():
    solution = Solution()
    assert solution.maxSubArray([2, 3, 5, 1, 3]).__eq__(14)
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]).__eq__(6)
    assert solution.maxSubArray([1]).__eq__(1)
    assert solution.maxSubArray([5, 4, -1, 7, 8]).__eq__(23)
    assert solution.maxSubArray([-2, -3, -1]).__eq__(-1)
