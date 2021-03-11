# use dfs (so-call backtracing) to enumerate all possible array combination
# and store them in one result array
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combination_results = []
        for i in range(0, len(candidates)):
            self.find_potential_result(candidates, i, target, [], combination_results)
        return combination_results

    def find_potential_result(self, candidates: List[int], index: int, target: int, potential_result: [], overall_result: []):
        potential_result.append(candidates[index])
        array_sum = self.get_array_sum(potential_result)
        if array_sum < target:
            for i in range(index, len(candidates)):
                self.find_potential_result(candidates, i, target, potential_result.copy(), overall_result)
        elif array_sum == target:
            overall_result.append(potential_result)

    def get_array_sum(self, nums: List[int]):
        result = 0
        for num in nums:
            result = result + num
        return result