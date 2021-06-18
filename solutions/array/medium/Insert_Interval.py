# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to
# their start times.


# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# Example 3:

# Input: intervals = [], newInterval = [5,7]
# Output: [[5,7]]
# Example 4:

# Input: intervals = [[1,5]], newInterval = [2,3]
# Output: [[1,5]]
# Example 5:

# Input: intervals = [[1,5]], newInterval = [2,7]
# Output: [[1,7]]
from typing import List
import logging

logger = logging.getLogger()


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        newIntervalIndex = -1
        # insert new interval
        for (index, interval) in enumerate(intervals):
            if interval[0] >= newInterval[0]:
                intervals.insert(index, newInterval)
                newIntervalIndex = index
                break

        if newIntervalIndex == -1:
            intervals.append(newInterval)
            newIntervalIndex = len(intervals) - 2

        merged = intervals[:newIntervalIndex]

        for interval in intervals:
            # not overlapping
            if not merged or merged[-1][-1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][-1] = max(merged[-1][-1], interval[1])

        return merged
