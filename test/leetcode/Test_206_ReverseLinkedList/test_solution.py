from leetcode.l206_ReverseLinkedList.Solution import Solution
from test.utilities import construct_linked_list
from test.utilities import linked_list_identical


def test_case1():
    head = construct_linked_list([1, 2, 3, 4, 5])
    ans = construct_linked_list([5, 4, 3, 2, 1])
    output = Solution.reverse_list(head)
    assert linked_list_identical(ans, output)


def test_case2():
    head = construct_linked_list([1, 2])
    ans = construct_linked_list([2, 1])
    output = Solution.reverse_list(head)
    assert linked_list_identical(ans, output)


def test_case3():
    head = construct_linked_list([])
    ans = construct_linked_list([])
    output = Solution.reverse_list(head)
    assert linked_list_identical(ans, output)
