from leetcode.l51_NQueens.Solution import Solution


def test_case1():
    n = 4
    output = Solution.solve_nqueens(n)
    assert sorted(output) == sorted([[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])


def test_case2():
    n = 1
    output = Solution.solve_nqueens(n)
    assert sorted(output) == sorted([["Q"]])
