from typing import List


class Solution:
    @staticmethod
    def min_path_sum(grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0 and i > 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                elif j != 0 and i != 0:
                    grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])
        return grid[m-1][n-1]