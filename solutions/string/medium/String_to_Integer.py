class Solution:
    def myAtoi(self, s: str) -> int:
        s = self.ignoreLeadingWhitespace(s)
        s = self.trimToValidInteger(s)
        s = self.removeLeadingZeros(s)

        if len(s) == 1 and s != '+' and s != '-':
            return int(s)

        return self.translate(s)

    def translate(self, s: str):
        positive = s[0] != '-'

        startIndex = 0
        if s[0] == '+' or s[0] == '-':
            startIndex = 1

        s = s[startIndex:]

        if positive:
            if len(s) > 10 or (len(s) == 10 and s > "2147483647"):
                return 2147483647
            else:
                return int(s)
        else:
            if len(s) > 10 or (len(s) == 10 and s >= "2147483648"):
                return -2147483648
            else:
                return -1 * int(s)

    def ignoreLeadingWhitespace(self, s: str):
        noWhitespaceIndex = 0
        for index, character in enumerate(s):
            if character != " ":
                noWhitespaceIndex = index
                break
        if s[noWhitespaceIndex:] == '':
            return "0"
        return s[noWhitespaceIndex:]

    def trimToValidInteger(self, s: str):
        startIndex = 0

        if s[0] == '+' or s[0] == '-':
            startIndex = 1

        for index in range(startIndex, len(s)):
            if s[index] not in '0123456789':
                s = s[0:index]
                break
        if s == '+' or s == '-' or s == '':
            return '0'
        return s

    def removeLeadingZeros(self, s: str):
        startIndex = 0

        symbol = ""

        if s[0] == '+' or s[0] == '-':
            startIndex = 1
            symbol = s[0]

        for index in range(startIndex, len(s)):
            if s[index] != '0':
                break
            startIndex = index
        s = s[startIndex:]
        return symbol + s
