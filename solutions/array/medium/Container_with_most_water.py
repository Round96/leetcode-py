class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxSpace=0
        start=0
        end=len(height) - 1
        while start < end:
            length = end - start
            space = min(height[start], height[end]) * length
            maxSpace = max(maxSpace, space)
            if height[start] < height[end]:
                start = start + 1
            else:                
                end = end - 1
        return maxSpace