from leetcode.l417_OceanWater.Solution1 import Solution


def test_case1():
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    output = Solution.pacific_atlantic(heights)
    assert output == list(set(map(tuple, [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])))


def test_case2():
    heights = [[1]]
    output = Solution.pacific_atlantic(heights)
    assert output == list(set(map(tuple, [[0, 0]])))
