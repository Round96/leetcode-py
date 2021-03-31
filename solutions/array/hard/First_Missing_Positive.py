# 41. First Missing Positive
# Hard

# 5445

# 965

# Add to List

# Share
# Given an unsorted integer array nums, find the smallest missing positive
# integer.


# Example 1:

# Input: nums = [1,2,0]
# Output: 3

# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2

# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1

# This solution mainly construct a exploration footprint records
# Given a object which defines the start and the end of the successive number we have explored and store them
# after each exploration, merge the successive numbers list

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        exploredNums = {}

        for num in nums:
            if num > 0:
                self.addFootprint(num, exploredNums)
                print(num, exploredNums)

        sorted_keys = sorted(exploredNums.keys())

        if len(sorted_keys) == 0 or sorted_keys[0] > 1:
            return 1
        else:
            return exploredNums[sorted_keys[0]]['end'] + 1

    def addFootprint(self, num, exploredNums):
        maxSmallerNum = -1
        for startIndex in list(exploredNums.keys()):
            # start index may be dynamically merged
            if not startIndex in exploredNums:
                continue

            if startIndex == num + 1:
                successiveNumbers = exploredNums[startIndex]
                successiveNumbers['start'] = num
                del exploredNums[startIndex]
                exploredNums[num] = successiveNumbers
                self.mergeSuccessiveNumbers(exploredNums)
                return
            elif startIndex < num:
                if startIndex > maxSmallerNum:
                    maxSmallerNum = startIndex
            elif startIndex == num:
                return
        if maxSmallerNum == -1:
            exploredNums[num] = {}
            exploredNums[num]['start'] = num
            exploredNums[num]['end'] = num
        else:
            successiveNumbers = exploredNums[maxSmallerNum]
            if successiveNumbers['end'] < num:
                if successiveNumbers['end'] + 1 == num:
                    successiveNumbers['end'] = num
                    exploredNums[maxSmallerNum] = successiveNumbers
                else:
                    exploredNums[num] = {}
                    exploredNums[num]['start'] = num
                    exploredNums[num]['end'] = num
        self.mergeSuccessiveNumbers(exploredNums)

    def mergeSuccessiveNumbers(self, exploredNums):
        # merge successive numbers
        for startIndex in list(exploredNums.keys()):
            # start index may be dynamically merged
            if not startIndex in exploredNums:
                continue
            endIndex = exploredNums[startIndex]['end']
            if (endIndex + 1) in exploredNums:
                successiveNumbersToBeMerged = exploredNums[endIndex + 1]
                del exploredNums[endIndex + 1]
                exploredNums[startIndex]['end'] = successiveNumbersToBeMerged['end']


# 这一题是discussion里的任务
# 他首先将所有的结果值缩小到0-len(nums)
# A：之后对每个数组里的num，利用 nums[ num % n]+=n 计算他们的num出现的评率，每出现一次就+=n
# 所以最后所有的nums，如果出现过了，则会>n
# 那么他是怎么解决最小这个的呢？
# 其实在A这一步，他就在构建从0-len(num)的有序数组了，这样最后输出的时候，只要输出最小的<n的那个数的下标就行了。

# def firstMissingPositive(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#      Basic idea:
#     1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
#         so we only have to care about those elements in this range and remove the rest.
#     2. we can use the array index as the hash to restore the frequency of each number within
#          the range [1,...,l+1]
#     """
#     nums.append(0)
#     n = len(nums)
#     for i in range(len(nums)): #delete those useless elements
#         if nums[i]<0 or nums[i]>=n:
#             nums[i]=0
#     for i in range(len(nums)): #use the index as the hash to record the frequency of each number
#         nums[nums[i]%n]+=n
#     for i in range(1,len(nums)):
#         if nums[i]/n==0:
#             return i
#     return n
