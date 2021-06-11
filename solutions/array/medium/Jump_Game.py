# Given an array of non-negative integers nums, you are initially
# positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that
# position.

# Determine if you are able to reach the last index.


# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum jump length is 0, which makes it impossible to reach the last
# index.


# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        for (index, num) in enumerate(nums):
            if num == 0 and index != length - 1:
                if not self.checkIfCanOnlyReachCurrentZeroPosition(
                        index, nums):
                    return False
        return True

    def checkIfCanOnlyReachCurrentZeroPosition(self, index, nums: List[int]):
        temp_index = index
        while temp_index >= 0:
            if nums[temp_index] > index - temp_index:
                return True
            temp_index -= 1
        return False
