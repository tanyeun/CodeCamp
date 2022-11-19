from leetcode.l769_MaxChunkToSort.Solution import Solution


def test_case1():
    arr = [4,3,2,1,0]
    output = Solution.max_chunks_to_sorted(arr)
    assert output == 1


def test_case2():
    arr = [1,0,2,3,4]
    output = Solution.max_chunks_to_sorted(arr)
    assert output == 4
