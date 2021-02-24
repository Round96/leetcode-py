class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        low, hi = 0, len(nums) - 1
        num_index = -1
        while low <= hi:
            mid = int((low + hi) / 2)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                num_index = mid
                break;
        if num_index == -1:
            return [-1, -1]

        start_index, end_index = num_index, num_index
        while start_index - 1 >= 0:
            if nums[start_index - 1] == nums[start_index]:
                start_index = start_index - 1
            else:
                break;
        while end_index + 1 <= len(nums) -1:
            if nums[end_index + 1] == nums[end_index]:
                end_index = end_index + 1
            else:
                break;
        return [start_index, end_index]