class Solution:
    def intToRoman(self, num: int) -> str:
        valueSteps = [1000, 500, 100, 50, 10, 5, 1]
        valueSymbol = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

        result = ''
        index = 0
        while index < len(valueSteps):
            divider = valueSteps[index]

            divideResult = int(num / divider)

            num = num - divider * divideResult

            if divideResult == 0:
                index += 2
                continue
            elif divideResult < 4:
                for i in range(divideResult):
                    result += valueSymbol[index]
            elif divideResult == 4:
                result += valueSymbol[index] + valueSymbol[index - 1]
            elif divideResult == 9:
                result += valueSymbol[index] + valueSymbol[index - 2]
            else:
                result += valueSymbol[index - 1]
                for i in range(divideResult - 5):
                    result += valueSymbol[index]

            index += 2

        return result
