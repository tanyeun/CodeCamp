from leetcode.l542_Matrix01.Solution import Solution


def test_case1():
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    output = Solution.update_matrix(mat)
    assert sorted(output) == sorted([[0,0,0],[0,1,0],[0,0,0]])


def test_case2():
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    output = Solution.update_matrix(mat)
    assert sorted(output) == sorted([[0,0,0],[0,1,0],[1,2,1]])


def test_case3():
    mat = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
    output = Solution.update_matrix(mat)
    assert sorted(output) == sorted([[0,1,0,1,2],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]])
