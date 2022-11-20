from typing import List
from collections import defaultdict
"""
Same algorithm as Solution, but pass all the test cases
"""


class Solution:
    @staticmethod
    def max_points(points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        def calcSlope(p1, p2):
            if p1[1] == p2[1]:
                return 0, p1[1]

            if p1[0] == p2[0]:
                return None, p1[0]

            m = (p2[1] - p1[1]) / (p2[0] - p1[0])
            c = p2[1] - m * p2[0]
            return (m, c)

        mp = defaultdict(lambda: set())
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                sl = calcSlope(points[i], points[j])
                mp[sl].add(i)
                mp[sl].add(j)

        return max([len(v) for v in mp.values()])
