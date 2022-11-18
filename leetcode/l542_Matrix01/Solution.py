from typing import List


class Solution:
    @staticmethod
    def update_matrix(mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = mat[:]
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    if i == 0 and j == 0:
                        dp[i][j] = 10000
                    elif i == 0:
                        dp[i][j] = mat[i][j - 1] + 1
                    elif j == 0:
                        dp[i][j] = mat[i - 1][j] + 1
                    else:
                        dp[i][j] = min(mat[i - 1][j], mat[i][j - 1]) + 1

        for x in range(m - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                if mat[x][y] != 0:
                    if x == m - 1 and y == n - 1:
                        mat[x][y] = dp[x][y]
                    elif x == m - 1:
                        mat[x][y] = min(dp[x][y], 1 + mat[x][y + 1])
                    elif y == n - 1:
                        mat[x][y] = min(dp[x][y], 1 + mat[x + 1][y])
                    else:
                        mat[x][y] = min(dp[x][y], 1 + min(mat[x + 1][y], mat[x][y + 1]))

        return mat