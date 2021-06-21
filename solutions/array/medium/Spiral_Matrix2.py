from typing import List
# import logging

# logger = logging.getLogger()


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        spiral_matrix = []
        for i in range(0, n):
            spiral_matrix.append([0] * n)
        for i in range(0, int((n + 1) / 2)):
            left_upper_num = self.get_the_left_upper_num(
                i, n)  # inner circle index starts from 0
            diagonal_sum = 2 * (left_upper_num + 2 * (n - 2 * i - 1))
            for j in range(i, n - i):
                spiral_matrix[i][j] = left_upper_num + j - i
                spiral_matrix[j][n - 1 - i] = left_upper_num + \
                    n - 2 * i - 1 + j - i

            for j in range(i + 1, n - i):
                spiral_matrix[j][i] = diagonal_sum - spiral_matrix[i][j]
                spiral_matrix[n - 1 - i][j] = diagonal_sum - \
                    spiral_matrix[j][n - 1 - i]

        return spiral_matrix

    def get_the_left_upper_num(self, inner_circle_index, matrix_length):
        result = 1
        for i in range(0, inner_circle_index):
            result += 4 * (matrix_length - 2 * i - 1)
        return result
