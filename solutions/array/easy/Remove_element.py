class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = 0
        for num in nums:
            if num != val:
                result += 1
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] != val:
                l += 1
            else:
                while nums[r] == val and r >= 0:
                    r -= 1
                if r > 0 and l < r:
                    temp = nums[l]
                    nums[l] = nums[r]
                    nums[r] = temp
        return result
        