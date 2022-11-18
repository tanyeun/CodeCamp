from typing import List


class Solution:
    @staticmethod
    def min_path_sum(grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        # 這個寫法不好，應為dp[0][0]寫入的同時，dp[1][0]也會被寫入
        #dp = [[0 for i in range(n)]] * m
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i ==0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
        return dp[m-1][n-1]