# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2
# ,...,yn].
#
#  Return the array in the form [x1,y1,x2,y2,...,xn,yn].
#
#
#  Example 1:
#
#
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,
# 5,4,1,7].
#
#
#  Example 2:
#
#
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
#
#
#  Example 3:
#
#
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]
#
#
#
#  Constraints:
#
#
#  1 <= n <= 500
#  nums.length == 2n
#  1 <= nums[i] <= 10^3
#  Related Topics Array
from typing import List


# Runtime: 652 ms, faster than 6.50% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions
# for Shuffle the Array.
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 1
        while i < n:
            self.forward_continuously_swap(nums, n - 1 + i, 2 * i - 1)
            i = i + 1
        return nums

    def forward_continuously_swap(
            self, nums: List[int], index: int, index_to_be_inserted_in: int):
        i = index
        while i > index_to_be_inserted_in:
            temp = nums[i]
            nums[i] = nums[i - 1]
            nums[i - 1] = temp
            i = i - 1

# Runtime: 112 ms, faster than 13.65% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Shuffle the Array.
#
# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         result = [0] * (2 * n);
#         i = 0
#         while i < n:
#             result[2 * i] = nums[i]
#             result[2 * i + 1] = nums[i + n]
#             i = i + 1
#         return result
