# You are given an n x n 2D matrix representing an image, rotate the image
# by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify
# the input 2D matrix directly. DO NOT allocate another 2D matrix and do
# the rotation.


# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# Example 3:

# Input: matrix = [[1]]
# Output: [[1]]
# Example 4:

# Input: matrix = [[1,2],[3,4]]
# Output: [[3,1],[4,2]]


# Constraints:

# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
from typing import List
import logging

logger = logging.getLogger()


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        square_rim = len(matrix)

        for i in range(int(square_rim / 2)):
            for j in range(i, i + (square_rim - 2 * i) - 1):
                self.rotate_number_in_square_rim(square_rim, matrix, (i, j))
                # logger.info(matrix)

    def rotate_number_in_square_rim(
            self, rim_length: int, matrix: List[List[int]], number_index: tuple):
        number_to_replace = -1001
        temp_number = matrix[number_index[0]][number_index[1]]
        for i in range(1, 5):
            if i == 1:
                number_to_replace = temp_number
                temp_number = matrix[number_index[1]][rim_length - 1 -
                                                      number_index[0]]
                matrix[number_index[1]][rim_length - 1 -
                                        number_index[0]] = number_to_replace
            if i == 2:
                number_to_replace = temp_number
                temp_number = matrix[rim_length -
                                     1 -
                                     number_index[0]][rim_length -
                                                      1 -
                                                      number_index[1]]
                matrix[rim_length - 1 - number_index[0]][rim_length -
                                                         1 - number_index[1]] = number_to_replace
            if i == 3:
                number_to_replace = temp_number
                temp_number = matrix[rim_length - 1 - number_index[1]
                                     ][number_index[0]]
                matrix[rim_length - 1 - number_index[1]
                       ][number_index[0]] = number_to_replace
            if i == 4:
                number_to_replace = temp_number
                matrix[number_index[0]][number_index[1]] = number_to_replace
