from leetcode.l91_DecodeWays.Solution1 import Solution


def test_case1():
    s= "12"
    output = Solution.num_decodings(s)
    assert output == 2


def test_case2():
    s= "226"
    output = Solution.num_decodings(s)
    assert output == 3


def test_case3():
    s= "06"
    output = Solution.num_decodings(s)
    assert output == 0

