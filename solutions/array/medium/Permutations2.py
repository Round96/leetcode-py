# Given a collection of numbers, nums, that might contain duplicates,
# return all possible unique permutations in any order.
from typing import List
import logging

logger = logging.getLogger()


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        return self.dfs(nums)

    def dfs(self, nums):
        result = []
        if len(nums) == 0:
            return [nums]

        # The difference between this method and the below is whether sort the
        # array first and skip the adjacent same number
        for (index, num) in enumerate(nums):
            if index != 0 and num == nums[index - 1]:
                continue

            temp_array = nums.copy()
            temp_array.remove(num)

            child_permutation_result = self.permuteUnique(temp_array)

            for partial_permutation in child_permutation_result:
                partial_permutation.append(num)
                result.append(partial_permutation)

        return result


# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         result = []

#         if len(nums) == 1:
#             return [nums]

#         for (index, num) in enumerate(nums):
#             if index != 0 and nums[index - 1] == nums:
#                 continue
#             temp_nums = nums.copy()
#             temp_nums.remove(num)

#             child_permutation_result = self.permuteUnique(temp_nums)

#             for partial_permutation in child_permutation_result:
#                 partial_permutation.append(num)

#                 if not (partial_permutation in result):
#                     result.append(partial_permutation)

#         return result
