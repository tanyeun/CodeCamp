class Solution:
    @staticmethod
    def fib(n):
        a = 1
        b = 1
        for i in range(2, n):
            a, b = b, a+b

        return b

