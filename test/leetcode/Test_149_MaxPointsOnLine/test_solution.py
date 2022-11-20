from leetcode.l149_MaxPointsOnLine.Solution2 import Solution
from test.utilities import plot_2d_list

def test_case1():
    points = [[1,1],[2,2],[3,3]]
    #plot_2d_list(points)
    output = Solution.max_points(points)
    assert output == 3


def test_case2():
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    #plot_2d_list(points)
    output = Solution.max_points(points)
    assert output == 4


def test_case3():
    points = [[0,0]]
    output = Solution.max_points(points)
    assert output == 1


def test_case4():
    points = [[0,1],[0,0]]
    output = Solution.max_points(points)
    assert output == 2


def test_case5():
    points = [[0,0],[1,1]]
    output = Solution.max_points(points)
    assert output == 2


def test_case6():
    points = [[3,3],[1,4],[1,1],[2,1],[2,2]]
    output = Solution.max_points(points)
    assert output == 3


def test_case7():
    points = [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]
    output = Solution.max_points(points)
    assert output == 5


def test_case8():
    points = [[7,3],[19,19],[-16,3],[13,17],[-18,1],[-18,-17],[13,-3],[3,7],[-11,12],[7,19],[19,-12],[20,-18],[-16,-15],[-10,-15],[-16,-18],[-14,-1],[18,10],[-13,8],[7,-5],[-4,-9],[-11,2],[-9,-9],[-5,-16],[10,14],[-3,4],[1,-20],[2,16],[0,14],[-14,5],[15,-11],[3,11],[11,-10],[-1,-7],[16,7],[1,-11],[-8,-3],[1,-6],[19,7],[3,6],[-1,-2],[7,-3],[-6,-8],[7,1],[-15,12],[-17,9],[19,-9],[1,0],[9,-10],[6,20],[-12,-4],[-16,-17],[14,3],[0,-1],[-18,9],[-15,15],[-3,-15],[-5,20],[15,-14],[9,-17],[10,-14],[-7,-11],[14,9],[1,-1],[15,12],[-5,-1],[-17,-5],[15,-2],[-12,11],[19,-18],[8,7],[-5,-3],[-17,-1],[-18,13],[15,-3],[4,18],[-14,-15],[15,8],[-18,-12],[-15,19],[-9,16],[-9,14],[-12,-14],[-2,-20],[-3,-13],[10,-7],[-2,-10],[9,10],[-1,7],[-17,-6],[-15,20],[5,-17],[6,-6],[-11,-8]]
    #plot_2d_list(points)
    output = Solution.max_points(points)
    assert output == 6