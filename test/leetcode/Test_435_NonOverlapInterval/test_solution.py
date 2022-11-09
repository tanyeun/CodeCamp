from leetcode.l435_NonOverlapInterval.Solution import Solution


def test_case1():
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    output = Solution.erase_overlap_intervals(intervals)
    assert output == 1


def test_case2():
    intervals = [[1, 2], [1, 2], [1, 2]]
    output = Solution.erase_overlap_intervals(intervals)
    assert output == 2


def test_case3():
    intervals = [[1, 2], [2, 3]]
    output = Solution.erase_overlap_intervals(intervals)
    assert output == 0