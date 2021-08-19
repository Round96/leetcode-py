from solutions.string.medium.Longest_Palindromic_Substring import Solution


def test():
    solution = Solution()
    assert solution.longestPalindrome("ab").__eq__('a')
    assert solution.longestPalindrome("abcabcbb").__eq__('bcb')
    assert solution.longestPalindrome("abba").__eq__('abba')
