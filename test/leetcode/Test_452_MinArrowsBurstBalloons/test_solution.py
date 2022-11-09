from leetcode.l88_MergeSortedArray.Solution import Solution


def test_case1():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_case2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    Solution.merge(nums1, m, nums2, n)
    assert nums1 == [1]


def test_case3():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    Solution.merge(nums1, m, nums2, n)
    assert nums1 == [1]
