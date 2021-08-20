class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = []
        for index in range(numRows):
            rows.append("")

        period = 2 * numRows - 2 - 1
        pathLength = 0
        for character in s:
            rowNum = self.getRowToInsert(pathLength, numRows)
            rows[rowNum] = rows[rowNum] + character
            if pathLength == period:
                pathLength = 0
            else:
                pathLength += 1

        result = ''
        for index in range(numRows):
            result = result + rows[index]

        return result

    def getRowToInsert(self, pathLength, numRows) -> int:
        if pathLength < numRows:
            return pathLength
        else:
            return (2 * numRows - 2 - pathLength)

# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1:
#             return s
#         rows = []
#         for index in range(numRows):
#             rows.append("")
#         for index, character in enumerate(s):
#             rowNum = self.getRowToInsert(index, numRows)
#             rows[rowNum] = rows[rowNum] + character

#         result = ''
#         for index in range(numRows):
#             result = result + rows[index]

#         return result

#     def getRowToInsert(self, index, numRows) -> int:
#         tempMediateRes = numRows * 2 - 2
#         m = index % tempMediateRes
#         if m >= numRows:
#             return tempMediateRes - m
#         return m
