class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        longestStr = ''
        for index in range(0, len(s) - 1):
            evenStr = self.getEvenLengthPalindrimeSubString(
                s, index, int(len(longestStr) / 2))
            oddStr = self.getOddLengthPalindrimeSubString(
                s, index, int(len(longestStr) / 2))

            if len(evenStr) > len(oddStr):
                if len(evenStr) > len(longestStr):
                    longestStr = evenStr
            else:
                if len(oddStr) > len(longestStr):
                    longestStr = oddStr

        return longestStr

    def getEvenLengthPalindrimeSubString(self, s: str, index, maxLength):
        offset = maxLength
        l, r = index - offset, index + offset + 1
        if s[l + 1: index + 1] != s[index +
                                    1: r][::-1]:
            return ''
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                offset += 1
            else:
                break
            l, r = index - offset, index + offset + 1

        return s[(index - offset + 1): (index + offset + 1)]

    def getOddLengthPalindrimeSubString(self, s: str, index, maxLength):
        offset = maxLength
        l, r = index - offset, index + offset
        if s[l: index] != s[index +
                            1: r + 1][::-1]:
            return ''
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                offset += 1
            else:
                break
            l, r = index - offset, index + offset

        return s[(l + 1): r]
