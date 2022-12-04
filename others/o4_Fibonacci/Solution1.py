

class Solution:
    @staticmethod
    def fib(n):
        cache = {}
        return Solution.helper(n, cache)

    @staticmethod
    def helper(n, cache):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n in cache:
            return cache[n]
        else:
            tmp = Solution.helper(n-1, cache) + Solution.helper(n-2, cache)
            cache[n] = tmp
            return tmp
