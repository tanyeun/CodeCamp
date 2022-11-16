from leetcode.l77_Combinations.Solution import Solution

def test_case1():
    n = 4
    k = 2
    output = Solution.combine(n, k)
    assert sorted(output) == sorted([[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])


def test_case2():
    n = 1
    k = 1
    output = Solution.combine(n, k)
    assert sorted(output) == sorted([[1]])
