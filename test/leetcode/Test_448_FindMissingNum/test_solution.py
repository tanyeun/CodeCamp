from leetcode.l448_FindMissingNum.Solution1 import Solution


def test_case1():
    nums = [4,3,2,7,8,2,3,1]
    output = Solution.find_disappeared_numbers(nums)
    assert output == [5,6]


def test_case2():
    nums = [1,1]
    output = Solution.find_disappeared_numbers(nums)
    assert output == [2]
