from leetcode.l23_MergeKList.Solution1 import Solution
from test.utilities import construct_linked_list
from test.utilities import linked_list_identical


def test_case1():
    head1 = construct_linked_list([1, 4, 5])
    head2 = construct_linked_list([1, 3, 4])
    head3 = construct_linked_list([2, 6])
    lists = [head1, head2, head3]

    output = Solution.merge_k_lists(lists)
    ans = construct_linked_list([1, 1, 2, 3, 4, 4, 5, 6])
    assert linked_list_identical(ans, output)

