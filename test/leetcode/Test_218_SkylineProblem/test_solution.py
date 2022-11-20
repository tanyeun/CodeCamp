from leetcode.l218_SkylineProblem.Solution import Solution


def test_case1():
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    output = Solution.get_skyline(buildings)
    assert output == [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]


def test_case2():
    buildings = [[0,2,3],[2,5,3]]
    output = Solution.get_skyline(buildings)
    assert output == [[0,3],[5,0]]


def test_case3():
    buildings = [[1,2,1],[1,2,2],[1,2,3]]
    output = Solution.get_skyline(buildings)
    assert output == [[1,3],[2,0]]
