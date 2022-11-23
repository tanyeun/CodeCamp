from others.o3_RollupTreeSum.Solution import Solution


def test_case1():
    tree =  [0, 0, 1, 1, 0, 4, 5, 5, 7, 5]
    data =  [0, 0, 10, 20, 0, 0, 0, 30, 40, 50]
    Solution.rollup(tree, data)
    assert data == [ 150, 30,  10, 20, 120, 120, 0, 70, 40, 50]