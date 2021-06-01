# Given an array of non-negative integers nums, you are initially
# positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that
# position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.


# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2
from typing import List
# import logging

# logger = logging.getLogger()


class Solution:
    def jump(self, nums: List[int]) -> int:
        # logger.info(nums)
        if len(nums) == 1:
            return 0
        index, jump_times = 0, 0

        while index + 1 + nums[index] < len(nums):
            temp_index = index
            index_in_nums = nums[index]
            largest_jump_length = 0
            # logger.info(nums[index + 1: index + 1 + index_in_nums])
            for (i, num) in enumerate(
                    nums[index + 1: index + 1 + index_in_nums]):
                if index_in_nums + num + i + 1 >= largest_jump_length:
                    largest_jump_length = index_in_nums + num + i + 1
                    index = temp_index + 1 + i
            jump_times += 1
            # logger.info((index, jump_times))
        return jump_times + 1
