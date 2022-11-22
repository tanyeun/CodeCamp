from others.o2_WhoMove.Solution import Solution


def test_case1():
    U = [10, 20, 30, 40, 50]
    V = [10, 30, 40, 50, 20]
    output = Solution.who_move(U, V)
    assert output == 4


def test_case2():
    U = [10, 20, 30, 40, 50]
    V = [10, 30, 40, 20, 50]
    output = Solution.who_move(U, V)
    assert output == 3


def test_case3():
    U = [10, 20, 30, 40, 50]
    V = [ 10, 30, 20, 40, 50]
    output = Solution.who_move(U, V)
    assert output ==  1 or output == 2