# Given an array of distinct integers candidates and a target integer
# target, return a list of all unique combinations of candidates where the
# chosen numbers sum to target. You may return the combinations in any
# order.

# The same number may be chosen from candidates an unlimited number of
# times. Two combinations are unique if the frequency of at least one of
# the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to
# target is less than 150 combinations for the given input.


# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
# Example 4:

# Input: candidates = [1], target = 1
# Output: [[1]]
# Example 5:

# Input: candidates = [1], target = 2
# Output: [[1,1]]


# Constraints:

# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500
# use dfs (so-call backtracing) to enumerate all possible array combination
# and store them in one result array

from typing import List


class Solution:
    def combinationSum(
            self, candidates: List[int], target: int) -> List[List[int]]:
        combination_results = []
        for i in range(0, len(candidates)):
            self.find_potential_result(
                candidates, i, target, [], combination_results)
        return combination_results

    def find_potential_result(
            self, candidates: List[int], index: int, target: int, potential_result: [], overall_result: []):
        potential_result.append(candidates[index])
        array_sum = self.get_array_sum(potential_result)
        if array_sum < target:
            for i in range(index, len(candidates)):
                self.find_potential_result(
                    candidates, i, target, potential_result.copy(), overall_result)
        elif array_sum == target:
            overall_result.append(potential_result)

    def get_array_sum(self, nums: List[int]):
        result = 0
        for num in nums:
            result = result + num
        return result
