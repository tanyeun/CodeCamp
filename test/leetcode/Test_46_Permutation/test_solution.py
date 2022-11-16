from leetcode.l46_Permutation.Solution import Solution
from collections import Counter

def test_case1():
    nums = [1, 2, 3]
    output = Solution.permute(nums)
    assert sorted(output) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])


def test_case2():
    nums = [0, 1]
    output = Solution.permute(nums)
    assert sorted(output) == sorted([[0,1],[1,0]])



def test_case3():
    nums = [1]
    output = Solution.permute(nums)
    assert sorted(output) == sorted([[1]])
