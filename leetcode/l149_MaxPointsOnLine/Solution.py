from typing import List
"""
  3 kinds of lines:
  1: y = ax + b            key = (a, b)
  2: y = b        dy = 0   key = ("INF", y)
  3: x = a        dx = 0   key = (0,x)
  book: (a,b) -> count
"""

class Solution:
    @staticmethod
    def max_points(points: List[List[int]]) -> int:
        book = {}
        max_count = 1
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                if dy == 0:
                    a = "INF"
                    b = points[i][1]
                else:
                    if dx == 0:
                        a = 0
                        b = points[i][0]
                    else:
                        a = float(dx)/float(dy)
                        b = points[i][1] - a * points[i][0]
                if (a, b) not in book:
                    book[(a, b)]=[points[i]]
                    book[(a, b)].append(points[j])
                else:
                    if points[i] not in book[(a, b)]:
                        book[(a, b)].append(points[i])
                    if points[j] not in book[(a, b)]:
                        book[(a, b)].append(points[j])
        for k, v in book.items():
            max_count = max(max_count, len(v))

        return max_count
