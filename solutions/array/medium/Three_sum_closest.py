class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        currentClosestSum = None
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if currentClosestSum is None:
                    currentClosestSum = s
                else:
                    if abs(target - s) < abs(target - currentClosestSum):
                        currentClosestSum = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return currentClosestSum


# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         currentClosestSum=None
#         firstNumIndex=0
#         for num in nums:
#             secondNumIndex=firstNumIndex + 1
#             thirdNumIndex=secondNumIndex + 1

#             while secondNumIndex < len(nums):
#                 while thirdNumIndex < len(nums):
#                     if currentClosestSum == None:
#                         currentClosestSum = num + nums[secondNumIndex] + nums[thirdNumIndex]
#                     else:
#                         sumNum = nums[firstNumIndex] + nums[secondNumIndex] + nums[thirdNumIndex]
#                         if abs(target - sumNum) < abs(target - currentClosestSum):
#                             currentClosestSum = sumNum
#                     thirdNumIndex = thirdNumIndex + 1
#                 secondNumIndex = secondNumIndex + 1
#                 thirdNumIndex = secondNumIndex + 1
#             firstNumIndex = firstNumIndex + 1
#         return currentClosestSum
