class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentLength = 0
        longestLength = 0
        visitedLetter = {}
        startIndex = 0
        for i, letter in enumerate(s):
            if letter in visitedLetter and visitedLetter[letter] >= startIndex:
                if currentLength > longestLength:
                    longestLength = currentLength
                currentLength = i - visitedLetter[letter]
                startIndex = visitedLetter[letter] + 1
                visitedLetter[letter] = i
            else:
                visitedLetter[letter] = i
                currentLength += 1

        return max(longestLength, currentLength)
