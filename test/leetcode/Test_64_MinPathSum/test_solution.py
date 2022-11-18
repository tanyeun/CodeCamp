from leetcode.l64_MinPathSum.Solution1 import Solution


def test_case1():
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    output = Solution.min_path_sum(grid)
    assert output == 7


def test_case2():
    grid = [[1,2,3],[4,5,6]]
    output = Solution.min_path_sum(grid)
    assert output == 12