
"""
The square of n^th positive integer can be represented as a sum
of first n odd positive integers.

n^2 = 1 + 3 + 5 + ... + 2*n-1
"""

# this solution is too slow based on Leetcode Judge
class Solution:
    @staticmethod
    def judge_square_sum(c: int) -> bool:
        a = 0
        while a*a <= c:
            b = c - a*a
            odd_sum = 0
            n = 1
            while odd_sum < b:
                odd_sum = odd_sum + n
                n += 2
            if odd_sum == b:
                return True
            a += 1
        return False

