from leetcode.l135_Candy.Solution import Solution
from test.utilities import timeit

@timeit
def test_case1():
    ratings = [1, 0, 2]
    output = Solution.candy(ratings)
    assert output == 5


def test_case2():
    ratings = [1, 2, 2]
    output = Solution.candy(ratings)
    assert output == 4


def test_case3():
    ratings = [1, 3, 4, 5, 2]
    output = Solution.candy(ratings)
    assert output == 11


def test_case4():
    ratings = [5, 4, 3, 2, 1]
    output = Solution.candy(ratings)
    assert output == 15
