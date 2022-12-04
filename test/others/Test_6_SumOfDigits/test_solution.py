from others.o6_SumOfDigits.Solution import Solution


def test_case1():
    n = 16
    output = Solution.digital_root(n)
    assert output == 7


def test_case2():
    n = 942
    output = Solution.digital_root(n)
    assert output == 6


def test_case3():
    n = 132189
    output = Solution.digital_root(n)
    assert output == 6

def test_case4():
    n = 493193
    output = Solution.digital_root(n)
    assert output == 2