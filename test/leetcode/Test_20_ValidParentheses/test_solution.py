from leetcode.l20_ValidParentheses.Solution import Solution


def test_case1():
    s = "()"
    output = Solution.is_valid(s)
    assert output is True


def test_case2():
    s = "()[]{}"
    output = Solution.is_valid(s)
    assert output is True


def test_case3():
    s = "(]"
    output = Solution.is_valid(s)
    assert output is False


def test_case4():
    s = "]"
    output = Solution.is_valid(s)
    assert output is False


def test_case5():
    s = "){"
    output = Solution.is_valid(s)
    assert output is False