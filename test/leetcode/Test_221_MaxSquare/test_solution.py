from leetcode.l221_MaxSquare.Solution import Solution


def test_case1():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    output = Solution.maximal_square(matrix)
    assert output == 4


def test_case2():
    matrix = [["0","1"],["1","0"]]
    output = Solution.maximal_square(matrix)
    assert output == 1


def test_case3():
    matrix = [["0"]]
    output = Solution.maximal_square(matrix)
    assert output == 0


def test_case4():
    matrix = [["0", "1"]]
    output = Solution.maximal_square(matrix)
    assert output == 1


def test_case5():
    matrix = [["1","1"],["1","1"]]
    output = Solution.maximal_square(matrix)
    assert output == 4


def test_case6():
    matrix = [["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]
    output = Solution.maximal_square(matrix)
    assert output == 16