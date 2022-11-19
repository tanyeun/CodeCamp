from leetcode.l241_DifferentWayAddParentheses.Solution import Solution


def test_case1():
    expression = "2-1-1"
    output = Solution.diff_ways_to_compute(expression)
    assert sorted(output) == sorted([0,2])


def test_case2():
    expression = "2*3-4*5"
    output = Solution.diff_ways_to_compute(expression)
    assert sorted(output) == sorted([-34,-14,-10,-10,10])