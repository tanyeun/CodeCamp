from leetcode.l239_SlidingWinMax.Solution1 import Solution


def test_case1():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    output = Solution.max_sliding_window(nums, k)
    assert output == [3,3,5,5,6,7]


def test_case2():
    nums = [1]
    k = 1
    output = Solution.max_sliding_window(nums, k)
    assert output == [1]
