from solutions.string.hard.Regular_Expression_Matching import Solution


def test():
    solution = Solution()
    assert solution.isMatch("a", ".*..a*").__eq__(False)
    assert solution.isMatch("ab", ".*").__eq__(True)
    assert solution.isMatch("bbbba", ".*a*a").__eq__(True)
    assert solution.isMatch(
        "aaaaaaaaaaaaab",
        "a*a*a*a*a*a*a*a*a*a*c").__eq__(False)
    assert solution.isMatch(
        "aabcbcbcaccbcaabc",
        ".*a*aa*.*b*.c*.*a*").__eq__(True)
    assert solution.isMatch("ab", ".*ab").__eq__(True)
    assert solution.isMatch("ab", ".*c").__eq__(False)
    assert solution.isMatch("a", ".*a").__eq__(True)
    assert solution.isMatch("a", "a").__eq__(True)
    assert solution.isMatch("aab", "c*a*b").__eq__(True)
    assert solution.isMatch("a", "a*").__eq__(True)
    assert solution.isMatch("a", "b").__eq__(False)
    assert solution.isMatch("a", "b*").__eq__(False)
    assert solution.isMatch("a", "ab*").__eq__(True)
    assert solution.isMatch("abcd", "abcd").__eq__(True)
    assert solution.isMatch("abcd", "abc").__eq__(False)
    assert solution.isMatch("", ".*").__eq__(True)
