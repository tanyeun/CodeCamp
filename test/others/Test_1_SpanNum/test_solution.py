from others.o1_SpanNum.Solution2 import Solution


def test_case1():
    nums = [0, 1, 0, 0, 1, 1, 0, 0, 0, 0]
    output = Solution.span(nums)
    assert output == [0, 3, 0, 0, 1, 5, 0, 0, 0, 0]