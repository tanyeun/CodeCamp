from leetcode.l934_ShortestBridge.Solution import Solution


def test_case1():
    grid = [[0,1],[1,0]]
    output = Solution.shortest_bridge(grid)
    assert output == 1


def test_case2():
    grid = [[0,1,0],[0,0,0],[0,0,1]]
    output = Solution.shortest_bridge(grid)
    assert output == 2

    
def test_case3():
    grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    output = Solution.shortest_bridge(grid)
    assert output == 1
