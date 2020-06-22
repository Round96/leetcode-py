# Given the array nums, for each nums[i] find out how many numbers in the array
# are smaller than it. That is, for each nums[i] you have to count the number of v
# alid j's such that j != i and nums[j] < nums[i].
#
#  Return the answer in an array.
#
#
#  Example 1:
#
#
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation:
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1).
# For nums[3]=2 there exist one smaller number than it (1).
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
#
#
#  Example 2:
#
#
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
#
#
#  Example 3:
#
#
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]
#
#
#
#  Constraints:
#
#
#  2 <= nums.length <= 500
#  0 <= nums[i] <= 100
#  Related Topics Array Hash Table


# Runtime: 164 ms, faster than 48.36% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 13.9 MB, less than 41.42% of Python3 online submissions
# for How Many Numbers Are Smaller Than the Current Number.
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arrays = [0] * 101
        for current_num in nums:
            arrays[current_num] = arrays[current_num] + 1
        result = [0] * len(nums)
        for index in range(0, len(nums)):
            for i in range(0, nums[index]):
                result[index] = arrays[i] + result[index]
        return result

# Runtime: 252 ms, faster than 46.76% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 13.7 MB, less than 90.16% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         result = []
#         for current_num in nums:
#             gtNums = 0
#             for num_to_compare in nums:
#                 if current_num > num_to_compare:
#                     gtNums = gtNums + 1
#             result.append(gtNums)
#         return result
