# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.


# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
from typing import List


class Solution:

    def combinationSum2(
            self, candidates: List[int], target: int) -> List[List[int]]:
        # for dropping duplicates
        backtracingPathRecords = {}

        candidates.sort()
        results = []

        for i in range(0, len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            self.backtracing(
                candidates,
                i,
                len(candidates),
                target,
                [],
                results,
                '', backtracingPathRecords)
        return results

    def backtracing(self, candidate: List[int], start_index: int, end_index: int,
                    target_num: int, potential_chain: [], result_list: List[List[int]], backtracingPath, backtracingPathRecords):
        for i in range(start_index, len(candidate)):
            tempPath = backtracingPath + str(candidate[i])
            if not tempPath in backtracingPathRecords:
                backtracingPathRecords[tempPath] = True
            else:
                continue
            if target_num == candidate[i]:
                potential_chain.append(candidate[i])
                result_list.append(potential_chain.copy())
                potential_chain.pop()
            elif target_num > candidate[i]:
                potential_chain.append(candidate[i])
                self.backtracing(
                    candidate,
                    i + 1,
                    end_index,
                    target_num - candidate[i],
                    potential_chain,
                    result_list,
                    backtracingPath + str(candidate[i]),
                    backtracingPathRecords)
                potential_chain.pop()
