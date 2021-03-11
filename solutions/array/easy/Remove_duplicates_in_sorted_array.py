class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastNum = None
        duplicatesIndexArray = []
        for num in nums:
            if lastNum is None:
                lastNum = num
                continue
            if lastNum == num:
                duplicatesIndexArray.append(num)
            lastNum = num

        for num in duplicatesIndexArray:
            nums.remove(num)
        return len(nums)
