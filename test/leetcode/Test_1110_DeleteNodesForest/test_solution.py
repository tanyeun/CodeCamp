from leetcode.l1110_DeleteNodesForest.Solution import Solution
from datastructure.my_tree import deserialize
from test.utilities import forest_equal_non_order


def test_case1():
    root = deserialize('[1,2,3,4,5,6,7]')
    to_delete = [3, 5]
    t1 = deserialize('[1,2,null,4]')
    t2 = deserialize('[6]')
    t3 = deserialize('[7]')
    output = Solution.del_nodes(root, to_delete)
    assert forest_equal_non_order(output, [t1, t2, t3])


def test_case2():
    root = deserialize('[1,2,4,null,3]')
    to_delete = [3]
    t1 = deserialize('[1,2,4]')
    output = Solution.del_nodes(root, to_delete)
    assert forest_equal_non_order(output, [t1])