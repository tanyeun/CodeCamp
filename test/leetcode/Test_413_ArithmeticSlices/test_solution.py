from leetcode.l413_ArithmeticSlices.Solution import Solution


def test_case1():
    nums = [1,2,3,4]
    output = Solution.number_of_arithmetic_slices(nums)
    assert output == 3


def test_case2():
    nums = [1]
    output = Solution.number_of_arithmetic_slices(nums)
    assert output == 0