# You're given strings J representing the types of stones that are jewels, and S
#  representing the stones you have. Each character in S is a type of stone you ha
# ve. You want to know how many of the stones you have are also jewels.
#
#  The letters in J are guaranteed distinct, and all characters in J and S are l
# etters. Letters are case sensitive, so "a" is considered a different type of sto
# ne from "A".
#
#  Example 1:
#
#
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
#
#
#  Example 2:
#
#
# Input: J = "z", S = "ZZ"
# Output: 0
#
#
#  Note:
#
#
#  S and J will consist of letters and have length at most 50.
#  The characters in J are distinct.
#
#  Related Topics Hash Table


# Runtime: 28 ms, faster than 77.01% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 13.8 MB, less than 72.83% of Python3 online submissions
# for Jewels and Stones.

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        original_length = len(S)
        for jewel in J:
            S = S.replace(jewel, '')
        return original_length - len(S)
