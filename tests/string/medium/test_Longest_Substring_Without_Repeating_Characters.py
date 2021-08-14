from solutions.string.medium.Longest_Substring_Without_Repeating_Characters import Solution


def test():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb").__eq__(3)
    assert solution.lengthOfLongestSubstring("").__eq__(0)
    assert solution.lengthOfLongestSubstring("adawswwww").__eq__(4)
    assert solution.lengthOfLongestSubstring("wwwwwwwwwww").__eq__(1)
    assert solution.lengthOfLongestSubstring("abba").__eq__(2)
    assert solution.lengthOfLongestSubstring("pwwkew").__eq__(3)
