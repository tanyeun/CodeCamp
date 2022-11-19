from typing import List

"""
1 2 3
4 5 6
7 8 9

先沿1-5-9對折
1 4 7
2 5 8
3 6 9

再一列一列反轉
7 4 1
8 5 2
9 6 3
"""
class Solution:
    @staticmethod
    def rotate(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
