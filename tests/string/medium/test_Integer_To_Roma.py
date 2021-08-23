from solutions.string.medium.Integer_to_Roman import Solution


def test():
    solution = Solution()
    assert solution.intToRoman(1).__eq__('I')
    assert solution.intToRoman(3).__eq__('III')
    assert solution.intToRoman(4).__eq__('IV')
    assert solution.intToRoman(5).__eq__('V')
    assert solution.intToRoman(6).__eq__('VI')
    assert solution.intToRoman(9).__eq__('IX')
    assert solution.intToRoman(10).__eq__('X')
    assert solution.intToRoman(58).__eq__('LVIII')
    assert solution.intToRoman(1994).__eq__('MCMXCIV')
