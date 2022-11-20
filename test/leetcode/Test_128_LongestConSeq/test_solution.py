from leetcode.l128_LongestConSeq.Solution1 import Solution


def test_case1():
    nums = [100,4,200,1,3,2]
    output = Solution.longest_consecutive(nums)
    assert output == 4


def test_case2():
    nums = [0,3,7,2,5,8,4,6,0,1]
    output = Solution.longest_consecutive(nums)
    assert output == 9

def test_case3():
    nums = [0,-1]
    output = Solution.longest_consecutive(nums)
    assert output == 2