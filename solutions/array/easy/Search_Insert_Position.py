# use binary search to locate the target possible index
# if it is found, return the index
# if it is not found, then separately check numbers in the range from
# start to end to determine its location
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)

        start, end = 0, length - 1

        while end - start > 1:
            mid = int((start + end) / 2)

            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                return mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            if target <= nums[start]:
                return start
            elif target > nums[start] and target < nums[end]:
                return start + 1
            else:
                return end + 1
