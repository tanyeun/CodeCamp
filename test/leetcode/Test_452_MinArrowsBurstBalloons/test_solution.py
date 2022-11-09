from leetcode.l452_MinArrowsBurstBalloons.Solution import Solution


def test_case1():
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    output = Solution.find_min_arrow_shots(points)
    assert output == 2


def test_case2():
    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    output = Solution.find_min_arrow_shots(points)
    assert output == 4


def test_case3():
    points = [[1, 2], [2, 3], [3, 4], [4, 5]]
    output = Solution.find_min_arrow_shots(points)
    assert output == 2


def test_case4():
    points = [[1, 2]]
    output = Solution.find_min_arrow_shots(points)
    assert output == 1


def test_case5():
    points = [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]
    output = Solution.find_min_arrow_shots(points)
    assert output == 2