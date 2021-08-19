class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        longestStr = ''
        for index in range(0, len(s) - 1):
            evenStr = self.getEvenLengthPalindrimeSubString(s, index)
            oddStr = self.getOddLengthPalindrimeSubString(s, index)

            if len(evenStr) > len(oddStr):
                if len(evenStr) > len(longestStr):
                    longestStr = evenStr
            else:
                if len(oddStr) > len(longestStr):
                    longestStr = oddStr

        return longestStr

    def getEvenLengthPalindrimeSubString(self, s: str, index):
        offset = 0
        l, r = index - offset, index + offset + 1
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                offset += 1
            else:
                break
            l, r = index - offset, index + offset + 1

        return s[(index - offset + 1): (index + offset + 1)]

    def getOddLengthPalindrimeSubString(self, s: str, index):
        offset = 1
        l, r = index - offset, index + offset
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                offset += 1
            else:
                break
            l, r = index - offset, index + offset

        return s[(index - offset + 1): (index + offset)]
