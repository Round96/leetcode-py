class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length > 1:
            comparationLengthStartFromEnd = 2

            while comparationLengthStartFromEnd <= length:
                subArray = nums[length - comparationLengthStartFromEnd : length]

                isAscent = self.checkIfArrayIsInAscendOrder(subArray)

                if isAscent:
                    comparationLengthStartFromEnd += 1
                    continue
                else:
                    numToBeCompared = subArray[0]

                    numToBeExchangedIntoBegin, numIndex = self.findNextBiggerNumInArray(numToBeCompared, subArray)

                    subArray[0] = numToBeExchangedIntoBegin
                    subArray[numIndex] = numToBeCompared

                    subSubArray = subArray[1: len(subArray)]

                    subSubArray.sort()

                    nums[length - comparationLengthStartFromEnd] = subArray[0]
                    for i in range(comparationLengthStartFromEnd - 1):
                        nums[length - comparationLengthStartFromEnd + 1 + i] = subSubArray[i]
                    break
            if comparationLengthStartFromEnd == length + 1:
                nums.sort()

    def checkIfArrayIsInAscendOrder(self, nums: List[int]):
        lastNum = None
        for num in nums:
            if lastNum != None:
                if lastNum >= num:
                    continue
                else:
                    return False
            else:
                lastNum = num
        return True
        
    def findNextBiggerNumInArray(self, val: int, nums: List[int]):
        result = -1, -1
        temp = -1
        index = -1
        for num in nums:
            index += 1
            if num > val:
                if temp == -1 or num < temp:
                    result = num, index
                    temp = num
        return result