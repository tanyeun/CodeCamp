
class Solution:
    @staticmethod
    def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        return Solution.fib(n-1) + Solution.fib(n-2)