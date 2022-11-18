from leetcode.l198_HouseRobber.Solution import Solution


def test_case1():
    nums = [1,2,3,1]
    output = Solution.rob(nums)
    assert output == 4


def test_case2():
    nums = [2,7,9,3,1]
    output = Solution.rob(nums)
    assert output == 12