from typing import List


class Solution:
    @staticmethod
    def find_min_arrow_shots(points: List[List[int]]) -> int:
        # Sort the Points based on the start Index
        points.sort(key=lambda x: x[0])
        prev = points[0]
        non_overlap = 1

        for s, e in points[1:]:
            if s > prev[1]:
                non_overlap += 1
                prev = [s, e]
            else:
                prev[1] = min(prev[1], e)

        return non_overlap
