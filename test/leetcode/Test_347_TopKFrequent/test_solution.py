from leetcode.l347_TopKFrequent.Solution import Solution


def test_case1():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    output = Solution.top_k_frequent(nums, k)
    assert output == [1, 2]


def test_case2():
    nums = [1]
    k = 1
    output = Solution.top_k_frequent(nums, k)
    assert output == [1]


def test_case3():
    nums = [-1, -1]
    k = 1
    output = Solution.top_k_frequent(nums, k)
    assert output == [-1]


def test_case4():
    nums = [1, 2]
    k = 2
    output = Solution.top_k_frequent(nums, k)
    assert output == [1, 2]


def test_case5():
    nums = [3, 0, 1, 0]
    k = 1
    output = Solution.top_k_frequent(nums, k)
    assert output == [0]