from leetcode.l167_TwoSum2.Solution import Solution


def test_case1():
    numbers = [2, 7, 11, 15]
    target = 9
    output = Solution.two_sum(numbers, target)
    assert output == [1, 2]


def test_case2():
    numbers = [2, 3, 4]
    target = 6
    output = Solution.two_sum(numbers, target)
    assert output == [1, 3]


def test_case3():
    numbers = [-1, 0]
    target = -1
    output = Solution.two_sum(numbers, target)
    assert output == [1, 2]
