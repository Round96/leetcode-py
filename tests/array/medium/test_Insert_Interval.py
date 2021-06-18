from solutions.array.medium.Insert_Interval import Solution


def test():
    solution = Solution()
    assert solution.insert([[1, 2], [3, 6], [8, 10], [15, 18]], [11, 15]).__eq__(
        [[1, 2], [3, 6], [8, 10], [11, 18]])
    assert solution.insert([[3, 6], [8, 10], [11, 18]], [1, 2]).__eq__(
        [[1, 2], [3, 6], [8, 10], [11, 18]])
    assert solution.insert([[3, 6], [8, 10], [11, 18]], [1, 4]).__eq__(
        [[1, 6], [8, 10], [11, 18]])
    assert solution.insert([[3, 6], [8, 10], [11, 18]], [19, 24]).__eq__(
        [[3, 6], [8, 10], [11, 18], [19, 24]])
    assert solution.insert([[3, 6], [8, 10], [11, 18]], [15, 24]).__eq__(
        [[3, 6], [8, 10], [11, 24]])
    assert solution.insert([[1, 3], [6, 9]], [2, 5]).__eq__([[1, 5], [6, 9]])
