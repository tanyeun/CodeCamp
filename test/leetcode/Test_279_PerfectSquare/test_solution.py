from leetcode.l279_PerfectSquare.Solution import Solution


def test_case1():
    n = 12
    output = Solution.num_squares(n)
    assert output == 3


def test_case2():
    n = 13
    output = Solution.num_squares(n)
    assert output == 2

def test_case3():
    n = 7927
    output = Solution.num_squares(n)
    assert output == 4
