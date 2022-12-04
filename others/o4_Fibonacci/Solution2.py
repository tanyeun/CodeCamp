

class Solution:
    @staticmethod
    def fib(n, cache=None):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if cache is None:
            cache = {}
        if n in cache:
            return cache[n]
        else:
            tmp = Solution.fib(n-1, cache) + Solution.fib(n-2, cache)
            cache[n] = tmp
            return tmp
