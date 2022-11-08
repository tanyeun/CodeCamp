from leetcode.l5_LongestPalindrome.Solution import Solution


def test_case1():
    s = "babad"
    output = Solution.longest_palindrome(s)
    assert output == "bab"