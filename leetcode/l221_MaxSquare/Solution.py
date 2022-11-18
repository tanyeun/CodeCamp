from typing import List


class Solution:
    @staticmethod
    def maximal_square(matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        max_len = 0
        dp = [[0]*n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                dp[x][y] = int(matrix[x][y])

        if matrix[0][0] == "1":
            max_len = 1
        if n >= 2:
            if matrix[0][1] == "1":
                max_len = 1
        if m >= 2:
            if matrix[1][0] == "1":
                max_len = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    tmp = min(dp[i-1][j], dp[i][j-1])
                    dp[i][j] = min(dp[i-1][j-1], tmp)+1
                max_len = max(max_len, dp[i][j])

        return max_len * max_len