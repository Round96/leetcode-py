import logging
logger = logging.getLogger()


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        patterns = self.splitPatternIntoMinorPattern(p)
        globalResult = {}
        return self.subMatch(s, 0, patterns, 0, globalResult)

    def subMatch(self, s: str, characterIndex,
                 patterns, patternIndex, globalResult):
        if characterIndex == len(s) and patternIndex == len(patterns):
            return True

        if characterIndex == len(s) and (patternIndex < len(
                patterns) - 1 and len(patterns[patternIndex]) == 1):
            return False

        if characterIndex != len(s) and patternIndex == len(patterns):
            return False

        character = s[characterIndex: characterIndex + 1]

        if len(patterns[patternIndex]) == 1:
            if character == patterns[patternIndex] or patterns[patternIndex] == '.':
                return self.getResultFromGlobalResultOrExecute(
                    s, characterIndex + 1, patterns, patternIndex + 1, globalResult)
            else:
                return False
        else:
            c = patterns[patternIndex][0]

            # return self.subMatch(s, characterIndex, patterns, patternIndex + 1) or (
            #     (c == '.' or c == s[characterIndex]) and self.subMatch(s, characterIndex + 1, patterns, patternIndex))
            if (character == c and character != '') or (
                    c == '.' and character != ''):
                return self.getResultFromGlobalResultOrExecute(s, characterIndex, patterns, patternIndex + 1, globalResult) \
                    or self.getResultFromGlobalResultOrExecute(s, characterIndex + 1, patterns, patternIndex, globalResult)
            else:
                return self.getResultFromGlobalResultOrExecute(
                    s, characterIndex, patterns, patternIndex + 1, globalResult)

    def getResultFromGlobalResultOrExecute(
            self, s, characterIndex, p, patternIndex, globalResult):
        if (characterIndex, patternIndex) in globalResult:
            return globalResult[(characterIndex, patternIndex)]
        globalResult[(characterIndex, patternIndex)] = self.subMatch(
            s, characterIndex, p, patternIndex, globalResult)
        return globalResult[(characterIndex, patternIndex)]

    def splitPatternIntoMinorPattern(self, p: str):
        patterns = []
        length = len(p)
        index = 0
        while index < length:
            if index != length - 1:
                if p[index + 1] == '*':
                    patterns.append(p[index: index + 2])
                    index += 2
                else:
                    patterns.append(p[index])
                    index += 1
            else:
                patterns.append(p[index])
                index += 1
        return patterns

    # def subMatch(self, s: str, patterns):
    #     if s == '' and patterns == '':
    #         return True

    #     if len(patterns) == 0 and len(s) != 0:
    #         return False

    #     if len(s) == 0 and (len(patterns) == 1 and (
    #             len(patterns) >= 2 and patterns[1] != '*')):
    #         return False

    #     if len(patterns) == 1:
    #         return len(s) == 1 and (s == patterns or patterns == '.')
    #     else:
    #         c1 = patterns[0]
    #         c2 = patterns[1]

    #         if c2 == '*':
    #             return self.subMatch(s, patterns[2:]) or (
    #                 (s != '' and (c1 == s[0] or c1 == '.')) and self.subMatch(s[1:], patterns))
    #         else:
    #             return (s != '' and (c1 == s[0] or c1 == '.')) and self.subMatch(
    #                 s[1:], patterns[1:])
