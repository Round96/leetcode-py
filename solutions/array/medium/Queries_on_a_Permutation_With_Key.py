# Given the array queries of positive integers between 1 and m, you have to proc
# ess all queries[i] (from i=0 to i=queries.length-1) according to the following r
# ules:
#
#
#  In the beginning, you have the permutation P=[1,2,3,...,m].
#  For the current i, find the position of queries[i] in the permutation P (inde
# xing from 0) and then move this at the beginning of the permutation P. Notice th
# at the position of queries[i] in P is the result for queries[i].
#
#
#  Return an array containing the result for the given queries.
#
#
#  Example 1:
#
#
# Input: queries = [3,1,2,1], m = 5
# Output: [2,1,2,1]
# Explanation: The queries are processed as follow:
# For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is 2, then we move 3
# to the beginning of P resulting in P=[3,1,2,4,5].
# For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is 1, then we move 1
# to the beginning of P resulting in P=[1,3,2,4,5].
# For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is 2, then we move 2
# to the beginning of P resulting in P=[2,1,3,4,5].
# For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is 1, then we move 1
# to the beginning of P resulting in P=[1,2,3,4,5].
# Therefore, the array containing the result is [2,1,2,1].
#
#
#  Example 2:
#
#
# Input: queries = [4,1,2,2], m = 4
# Output: [3,1,2,0]
#
#
#  Example 3:
#
#
# Input: queries = [7,5,5,8,3], m = 8
# Output: [6,5,0,7,5]
#
#
#
#  Constraints:
#
#
#  1 <= m <= 10^3
#  1 <= queries.length <= m
#  1 <= queries[i] <= m
#  Related Topics Array


# Runtime: 136 ms, faster than 22.67% of Python3 online submissions for Queries on a Permutation With Key.
# Memory Usage: 14.1 MB, less than 31.15% of Python3 online submissions
# for Queries on a Permutation With Key.
from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result = []
        permutation_array = [0] * m

        i = 1
        while i <= m:
            permutation_array[i - 1] = i
            i = i + 1

        for element in queries:
            result.append(self.find_certain_number_in_array(
                permutation_array, element))

            permutation_array.remove(element)
            permutation_array.insert(0, element)

        return result

    def find_certain_number_in_array(
            self, nums: List[int], num_to_be_found: int):
        for index, element in enumerate(nums):
            if element == num_to_be_found:
                return index

# Runtime: 136 ms, faster than 22.67% of Python3 online submissions for Queries on a Permutation With Key.
# Memory Usage: 13.9 MB, less than 84.90% of Python3 online submissions for Queries on a Permutation With Key.
# class Solution:
#     def processQueries(self, queries: List[int], m: int) -> List[int]:
#         result = []
#         permutation_array = [1]

#         i = 1
#         while i <= m:
#             i = i + 1
#             permutation_array.append(i)


#         for element in queries:
#             result.append(self.find_certain_number_in_array(permutation_array, element))
#             permutation_array.remove(element)
#             permutation_array.insert(0, element)

#         return result

#     def find_certain_number_in_array(self, nums: List[int], num_to_be_found: int):
#         for index, element in enumerate(nums):
#             if element == num_to_be_found:
#                 return index
