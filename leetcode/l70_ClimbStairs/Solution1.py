

# this is like fibonacci seq
class Solution:
    @staticmethod
    def climb_stairs(n: int) -> int:
        pre = cur = 1
        for i in range(n - 1):
            pre, cur = cur, pre + cur
        return cur
