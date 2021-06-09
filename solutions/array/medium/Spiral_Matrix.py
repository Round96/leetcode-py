# Given an m x n matrix, return all elements of the matrix in spiral order.


# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
from typing import List
import logging

logger = logging.getLogger()


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        row_length = len(matrix)
        column_length = len(matrix[0])
        if row_length == 1:
            return matrix[0]
        if column_length == 1:
            for index in range(0, row_length):
                result.append(matrix[index][0])
            return result
        for row in range(0, int((row_length + 1) / 2)):
            if row * 2 + 1 > column_length:
                break
            if (column_length - row * 2) / \
                    2 == 0.5 and row_length > column_length:
                for index in range(row, row_length - row):
                    result.append(matrix[index][column_length - 1 - row])
                logger.info(result)
                return result
            else:
                result = result + self.spiral_once(
                    matrix,
                    row,
                    row,
                    row_length,
                    column_length)
            logger.info(result)

        return result

    def spiral_once(
            self, matrix: List[List[int]], start_row, start_column, row_length, column_length):
        top, right, bottom, left = True, True, True, True

        if start_row == int(row_length / 2):
            if row_length % 2 == 1:
                right = False
                bottom = False
                left = False

        spiral_once_result = []

        if top:
            for index in range(start_column, column_length - start_row):
                spiral_once_result.append(matrix[start_row][index])

        if right:
            for index in range(start_row + 1, row_length - start_row):
                spiral_once_result.append(
                    matrix[index][column_length - 1 - start_column])

        if bottom:
            temp_arr = []
            for index in range(start_column, column_length - start_column - 1):
                temp_arr.append(matrix[row_length - 1 - start_row][index])
            temp_arr.reverse()
            spiral_once_result = spiral_once_result + temp_arr

        if left:
            temp_arr = []
            for index in range(start_row + 1, row_length - start_row - 1):
                temp_arr.append(matrix[index][start_column])
            temp_arr.reverse()
            spiral_once_result = spiral_once_result + temp_arr

        return spiral_once_result
