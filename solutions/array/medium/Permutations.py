# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
from typing import List
import logging

logger = logging.getLogger()


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums]

        for num in nums:
            temp_array = nums.copy()
            temp_array.remove(num)

            for potential_combination in self.permute(temp_array):
                result.append([num] + potential_combination)

        return result
