class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        startNum=self.findMinNum(nums)
        endNum=self.findMaxNum(nums)

        average = int((startNum + endNum) / 2)
        while endNum - 1 > startNum:
            smallerBasket=0
            largerBasket=0
            for num in nums:
                if num >= startNum and num <= endNum:
                    if num <= average:
                        smallerBasket = smallerBasket + 1
                    else:
                        largerBasket = largerBasket + 1
            if smallerBasket == largerBasket:
                if average - startNum >= endNum - average:
                    startNum = average
                else:
                    endNum = average
            elif smallerBasket > largerBasket:
                endNum = average
            else:
                startNum = average

            average = int((startNum + endNum) / 2)
        if startNum == endNum:
            return startNum
        else:
            startNumShownNum = 0
            endNumShownNum = 0
            for num in nums:
                if num == startNum:
                    startNumShownNum = startNumShownNum + 1
                if num == endNum:
                    endNumShownNum = endNumShownNum + 1
            if startNumShownNum > endNumShownNum:
                return startNum
            else:
                return endNum

    def findMaxNum(self, nums: List[int]) -> int:
        maxNum = 0
        for num in nums:
            if maxNum < num:
                maxNum = num

        return maxNum

    def findMinNum(self, nums: List[int]) -> int:
        minNum = len(nums)
        for num in nums:
            if minNum > num:
                minNum = num

        return minNum


# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         numMap = {}
#         for num in nums:
#             if num in numMap:
#                 return num
#             numMap[num] = 1