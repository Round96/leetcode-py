class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.inner_search(nums, target, 0, len(nums) - 1)

    # start_index is included, end_index is also included
    def inner_search(
            self, nums: List[int], target: int, start_index: int, end_index: int) -> int:
        if start_index + 1 == end_index or start_index == end_index:
            if nums[start_index] == target:
                return start_index
            elif nums[end_index] == target:
                return end_index
            else:
                return -1
        # if this list is sorted
        if nums[start_index] < nums[end_index]:
            medium_index = int((end_index + start_index) / 2)
            if nums[medium_index] > target:
                return self.inner_search(
                    nums, target, start_index, medium_index)
            elif nums[medium_index] < target:
                return self.inner_search(nums, target, medium_index, end_index)
            else:
                return medium_index
        # if this list is rotated
        elif nums[start_index] > nums[end_index]:
            medium_index = int((end_index + start_index) / 2)
            if nums[start_index] < nums[medium_index]:
                if target < nums[start_index]:
                    return self.inner_search(
                        nums, target, medium_index, end_index)
                else:
                    if target > nums[medium_index]:
                        return self.inner_search(
                            nums, target, medium_index, end_index)
                    else:
                        return self.inner_search(
                            nums, target, start_index, medium_index)
            else:
                if target < nums[medium_index]:
                    return self.inner_search(
                        nums, target, start_index, medium_index)
                else:
                    if nums[start_index] > target:
                        return self.inner_search(
                            nums, target, medium_index, end_index)
                    else:
                        return self.inner_search(
                            nums, target, start_index, medium_index)
