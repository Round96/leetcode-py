from solutions.string.medium.ZigZag_Conversion import Solution


def test():
    solution = Solution()
    assert solution.convert("PAYPALISHIRING", 3).__eq__('PAHNAPLSIIGYIR')
