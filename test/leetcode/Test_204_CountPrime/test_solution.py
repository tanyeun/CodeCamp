from leetcode.l204_CountPrime.Solution import Solution


def test_case1():
    n = 10
    output = Solution.count_primes(n)
    assert output == 4


def test_case2():
    n = 0
    output = Solution.count_primes(n)
    assert output == 0


def test_case3():
    n = 1
    output = Solution.count_primes(n)
    assert output == 0
