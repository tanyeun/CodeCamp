from typing import List


class Solution:
    @staticmethod
    def erase_overlap_intervals(intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x[1])

        removed = 0; prev = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev:
                removed += 1
            else:
                prev = intervals[i][1]
        return removed