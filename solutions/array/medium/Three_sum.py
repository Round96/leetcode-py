from typing import List

# 这种做法虽然可以解决，但是复杂度很高，比如在2个负数和1个正数的计算过程中，为了得到特定的两个负数之和，它相当于做了一次n*n的
# 遍历，整个算法复杂度可达 n*n*n
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) < 3:
#             return []
#         result = []
#         nums.sort()

#         if nums[0] > 0 or nums[len(nums) - 1] < 0:
#             return []
        
#         zeroMet = False
#         zeroNums = 0
#         negativeEndAt = 0
#         positiveStartAt = len(nums)
#         for index, num in enumerate(nums):
#             if num == 0:
#                 zeroNums = zeroNums + 1
#             if num == 0 and not zeroMet:
#                 zeroMet = True
#                 negativeEndAt = index 
#             elif num > 0:
#                 if not zeroMet:
#                     negativeEndAt = index
#                 positiveStartAt = index
#                 break
        
        
#         negs = nums[0: negativeEndAt]
#         poss = nums[positiveStartAt: len(nums)]

#         # if we have two negative num and one possitive num
#         if len(negs) >= 2 and len(poss) >= 1:
#             index1 = 0
#             index2 = 1
#             index3 = len(poss) - 1
#             while index3 >= 0:
#                 print(index3)
#                 negSum = negs[index1] + negs[index2]
#                 posSum = poss[index3]
#                 numSum = negSum + posSum
#                 if numSum == 0:
#                     result.append([negs[index1], negs[index2], poss[index3]])
#                     while True:
#                         if index2 < len(negs) - 1 and negs[index2 + 1] == negs[index2]:
#                             index2 = index2 + 1
#                         else:
#                             break
#                     while True:
#                         if index1 < index2 - 1 and negs[index1 + 1] == negs[index1]:
#                             index1 = index1 + 1
#                         else:
#                             break
#                 if index1 == index2 - 1 and index2 == len(negs) - 1:
#                     # ignore duplicated nums
#                     while True:
#                         if index3 > 0 and poss[index3 - 1] == poss[index3]:
#                             index3 = index3 - 1
#                         else:
#                             break
#                     # new loop
#                     index3 = index3 - 1
#                     index1 = 0
#                     index2 = 1
#                 elif negs[index1] + poss[index3] < 0 or negs[index1] + negs[len(negs) - 1] + poss[index3] < 0:
#                     # new loop
#                     index1 = index1 + 1
#                     index2 = index1 + 1
#                 else:
#                     if index2 == len(negs) - 1 or numSum > 0:
#                         index1 = index1 + 1
#                         index2 = index1 + 1
#                     else:
#                         index2 = index2 + 1

#         # if we have zero and one neg and one pos
#         if zeroMet:
#             index1 = 0
#             index2 = len(poss) - 1
#             while index1 < len(negs) and index2 >= 0:
#                 if negs[index1] + poss[index2] == 0:
#                     result.append([0, negs[index1], poss[index2]])
#                     # ignore duplicated nums
#                     while True:
#                         if index1 < len(negs) - 1 and negs[index1 + 1] == negs[index1]:
#                             index1 = index1 + 1
#                         else:
#                             break
#                     while True:
#                         if index2 >= 1 and poss[index2 - 1] == poss[index2]:
#                             index2 = index2 - 1
#                         else:
#                             break
#                 if index1 == len(negs) - 1:
#                     index2 = index2 - 1
#                 elif index2 == 0:
#                     index1 = index1 + 1
#                 else:
#                     if -negs[index1] > poss[index2]:
#                         index1 = index1 + 1
#                     else:
#                         index2 = index2 - 1

#         # if we have many zero >= 3
#         if zeroNums >= 3:
#             result.append([0, 0, 0])
#         # if we have one negative num and two possitive num
#         if len(poss) >= 2 and len(negs) >= 1:
#             index1 = len(negs) - 1
#             index2 = 0
#             index3 = 1
#             while index1 >= 0:
#                 negSum = negs[index1]
#                 posSum = poss[index2] + poss[index3]
#                 numSum = negSum + posSum

#                 if numSum == 0:
#                     result.append([negs[index1], poss[index2], poss[index3]])
#                     # ignore duplicated records
#                     while True:
#                         if index3 < len(poss) - 1 and poss[index3 + 1] == poss[index3]:
#                             index3 = index3 + 1
#                         else:
#                             break
#                     while True:
#                         if index3 > index2 + 1 and poss[index2 + 1] == poss[index2]:
#                             index2 = index2 + 1
#                         else:
#                             break
#                 if index2 == index3 - 1 and index3 == len(poss) - 1:
#                     # ignore duplicated nums
#                     while True:
#                         if index1 > 0 and negs[index1 - 1] == negs[index1]:
#                             index1 = index1 - 1
#                         else:
#                             break
#                     # new loop
#                     index1 = index1 - 1
#                     index2 = 0
#                     index3 = 1
#                 else:
#                     if index3 == len(poss) - 1 or numSum > 0:
#                         index2 = index2 + 1
#                         index3 = index2 + 1
#                     else:
#                         index3 = index3 + 1
#         return result
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res