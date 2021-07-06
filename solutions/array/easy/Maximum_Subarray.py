# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.


# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23


# Constraints:

# 1 <= nums.length <= 3 * 104
# -105 <= nums[i] <= 105
from typing import List


class Solution:

    # using divide and conquer
    def maxSubArray(self, nums: List[int]) -> int:
        return self.findMaxSubArray(nums, 0, len(nums) - 1)

    def findMaxSubArray(self, nums: List[int], left, right):
        if right == left:
            return nums[left]

        if left + 1 == right:
            return max(max(nums[left], nums[right]), nums[left] + nums[right])

        mid = int((left + right) / 2)

        maxLeftSum = self.findMaxSubArray(nums, left, mid)
        maxRightSum = self.findMaxSubArray(nums, mid + 1, right)
        maxCrossingSum = self.findCrossMaxSubArray(nums, left, mid, right)

        return max(max(maxLeftSum, maxRightSum), maxCrossingSum)

    def findCrossMaxSubArray(self, nums: List[int], left, mid, right):
        leftSum = 0
        maxLeftSum = -105
        for i in range(mid - left + 1):
            leftSum += nums[mid - i]
            if maxLeftSum < leftSum:
                maxLeftSum = leftSum

        rightSum = 0
        maxRightSum = -105
        for i in range(right - mid + 1):
            rightSum += nums[mid + i]
            if maxRightSum < rightSum:
                maxRightSum = rightSum

        return max(max(maxLeftSum, maxRightSum),
                   maxLeftSum + maxRightSum - nums[mid])

    # using dp alogrithm

    def maxSubArray_DP(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)
