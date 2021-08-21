from solutions.string.medium.String_to_Integer import Solution


def test():
    solution = Solution()
    assert solution.myAtoi("").__eq__(0)
    assert solution.myAtoi("      ").__eq__(0)
    assert solution.myAtoi("42").__eq__(42)
    assert solution.myAtoi("+0123").__eq__(123)
    assert solution.myAtoi("-0123").__eq__(-123)
    assert solution.myAtoi("words and 987").__eq__(0)
    assert solution.myAtoi("   +   2147483647").__eq__(0)
    assert solution.myAtoi("2147483647").__eq__(2147483647)
    assert solution.myAtoi("2147483648").__eq__(2147483647)
    assert solution.myAtoi("-2147483648").__eq__(-2147483648)
    assert solution.myAtoi("-2147483649").__eq__(-2147483648)
    assert solution.myAtoi("    0000000000000   ").__eq__(0)
