from leetcode.l240_Search2DMatrix2.Solution import Solution


def test_case1():
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    output = Solution.search_matrix(matrix, target)
    assert output is True


def test_case2():
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 20
    output = Solution.search_matrix(matrix, target)
    assert output is False


def test_case3():
    matrix = [[-5]]
    target = -5
    output = Solution.search_matrix(matrix, target)
    assert output is True
