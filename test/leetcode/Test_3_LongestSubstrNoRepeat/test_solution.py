from leetcode.l3_LongestSubstrNoRepeat.Solution1 import Solution
from test.utilities import pair_equal_non_order
import timeit

def test_case1():
    s = "abcabcbb"
    output = Solution.length_of_longest_substring(s)
    assert output == 3


def test_case2():
    s = "bbbbb"
    output = Solution.length_of_longest_substring(s)
    assert output == 1


def test_case3():
    s = "pwwkew"
    output = Solution.length_of_longest_substring(s)
    assert output == 3

def test_case4():
    s = " "
    output = Solution.length_of_longest_substring(s)
    assert output == 1

# Sol1: 1.200009137392044e-06 / 10 iterations
#       4.999979864805937e-06 / 100
#       8.849991718307137e-05 / 1000
# Sol:  1.200009137392044e-06 / 10
#       6.100046448409557e-06 / 100
#       0.00011430005542933941 / 1000
def test_time():
    iterations = 1000
    t1 = timeit.timeit('test_case1', number=iterations, globals=globals())
    t2 = timeit.timeit('test_case2', number=iterations, globals=globals())
    t3 = timeit.timeit('test_case3', number=iterations, globals=globals())
    t4 = timeit.timeit('test_case4', number=iterations, globals=globals())
    print("execution: ", t1+t2+t3+t4)