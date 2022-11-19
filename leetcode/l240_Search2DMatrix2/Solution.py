from typing import List


class Solution:
    @staticmethod
    def search_matrix(matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)     # rows
        n = len(matrix[0])  # cols

        r = 0
        c = n-1

        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1

        return False
