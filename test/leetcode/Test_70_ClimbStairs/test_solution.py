from leetcode.l70_ClimbStairs.Solution1 import Solution


def test_case1():
    n = 2
    output = Solution.climb_stairs(n)
    assert output == 2


def test_case2():
    n = 3
    output = Solution.climb_stairs(n)
    assert output == 3

def test_case3():
    n = 4
    output = Solution.climb_stairs(n)
    assert output == 5