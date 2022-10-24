from leetcode.l3_LongestSubstrNoRepeat.Solution1 import Solution
from test.utilities import pair_equal_non_order


def test_case1():
    s = "abcabcbb"
    output = Solution.length_of_longest_substring(s)
    assert output == 3


def test_case2():
    s = "bbbbb"
    output = Solution.length_of_longest_substring(s)
    assert output == 1


def test_case3():
    s = "pwwkew"
    output = Solution.length_of_longest_substring(s)
    assert output == 3

def test_case4():
    s = " "
    output = Solution.length_of_longest_substring(s)
    assert output == 1
