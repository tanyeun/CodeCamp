from typing import List


class Solution:
    @staticmethod
    def max_area_island(grid: List[List[int]]) -> int:
        # this helper function is performing DFS
        def area(r, c):
            # 直接return 0:
            #    grid[r][c] == 0 : 沒有面積
            #    grid[r][c] 超出範圍
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and grid[r][c]):
                return 0
            grid[r][c] = 0  # 計算過面積的點歸零
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))
