from leetcode.l215_KthLargestElementInArray.Solution import Solution


def test_case1():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    output = Solution.find_kth_largest(nums, k)
    assert output == 5


def test_case2():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    output = Solution.find_kth_largest(nums, k)
    assert output == 4


def test_case3():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    output = Solution.find_kth_minimum(nums, k)
    assert output == 2


def test_case4():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 3
    output = Solution.find_kth_minimum(nums, k)
    assert output == 2