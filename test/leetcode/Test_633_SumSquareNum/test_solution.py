from leetcode.l633_SumSquareNum.Solution import Solution


def test_case1():
    c = 5
    output = Solution.judge_square_sum(c)
    assert output is True


def test_case2():
    c = 3
    output = Solution.judge_square_sum(c)
    assert output is False
