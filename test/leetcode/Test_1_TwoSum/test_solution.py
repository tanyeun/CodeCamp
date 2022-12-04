from leetcode.l1_TwoSum.Solution import Solution
from test.utilities import pair_equal_non_order
import timeit

def test_case1():
    nums = [2, 7, 11, 15]
    target = 9
    output = Solution.two_sum(nums, target)
    assert pair_equal_non_order(output, [0, 1])


def test_case2():
    nums = [3, 2, 4]
    target = 6
    output = Solution.two_sum(nums, target)
    assert pair_equal_non_order(output, [1, 2])


def test_case3():
    nums = [3, 3]
    target = 6
    output = Solution.two_sum(nums, target)
    assert pair_equal_non_order(output, [0, 1])

def test_time():
    t1 = timeit.timeit('test_case1', number=100, globals=globals())
    t2 = timeit.timeit('test_case2', number=100, globals=globals())
    t3 = timeit.timeit('test_case3', number=100, globals=globals())
    print("execution: ", t1+t2+t3)