from leetcode.l680_ValidPalindrome2.Solution import Solution


def test_case1():
    s = "aba"
    output = Solution.valid_palindrome(s)
    assert output is True


def test_case2():
    s = "abca"
    output = Solution.valid_palindrome(s)
    assert output is True

def test_case3():
    s = "abc"
    output = Solution.valid_palindrome(s)
    assert output is False