
# Given n non-negative integers representing an elevation map where the
# width of each bar is 1, compute how much water it can trap after
# raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


# Constraints:

# n == height.length
# 0 <= n <= 3 * 104
# 0 <= height[i] <= 105
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        left_first_barrier = 0
        right_first_barrier = len(height) - 1

        total_trapped_water = 0

        # first find the actual exitsted barrier
        while height[left_first_barrier] == 0:
            left_first_barrier += 1
        while height[right_first_barrier] == 0:
            right_first_barrier -= 1

        while left_first_barrier < right_first_barrier:
            l = left_first_barrier
            r = right_first_barrier
            if height[left_first_barrier] < height[right_first_barrier]:
                while l < right_first_barrier and height[left_first_barrier] >= height[l]:
                    total_trapped_water += height[left_first_barrier] - height[l]
                    l += 1
                left_first_barrier = l
            else:
                while left_first_barrier < r and height[right_first_barrier] >= height[r]:
                    total_trapped_water += height[right_first_barrier] - height[r]
                    r -= 1
                right_first_barrier = r

        return total_trapped_water


# 这个方法是从下往上一层层计算空余水位并且进行累加
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         total_count_of_trapped_water = 0
#         has_water = True
#         while has_water:
#             layer_water = []
#             for num in height:
#                 layer_water.append(0)
#             has_water = False
#             for index, num in enumerate(height):
#                 if num > 0:
#                     layer_water[index] = 1
#                     height[index] = height[index] - 1
#                     has_water = True
#             total_count_of_trapped_water += self.calculate_trapped_water_in_one_layer(
#                 layer_water)
#         return total_count_of_trapped_water

#     def calculate_trapped_water_in_one_layer(self, height: List[int]) -> int:
#         left_barrier = None
#         layer_trapped_water = 0
#         for index, num in enumerate(height):
#             if num == 1:
#                 if left_barrier is None:
#                     # first encounter the barrier
#                     left_barrier = index
#                 else:
#                     layer_trapped_water += index - left_barrier - 1
#                     left_barrier = index
#         return layer_trapped_water
