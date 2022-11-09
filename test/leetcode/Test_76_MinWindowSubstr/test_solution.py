from leetcode.l76_MinWindowSubstr.Solution import Solution


def test_case1():
    s = "ADOBECODEBANC"
    t = "ABC"
    output = Solution.min_window(s, t)
    assert output == "BANC"


def test_case2():
    s = "a"
    t = "a"
    output = Solution.min_window(s, t)
    assert output == "a"


def test_case3():
    s = "a"
    t = "aa"
    output = Solution.min_window(s, t)
    assert output == ""
