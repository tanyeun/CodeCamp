from others.o7_DeleteDLLnode.Solution import Solution
from test.utilities import construct_double_linked_list
from test.utilities import double_linked_list_identical

def test_case1():
    head = construct_double_linked_list([1, 3, 5, 7, 9])
    ans = construct_double_linked_list([1, 3, 7, 9])
    output = Solution.delete_dllnode(head, 5)
    assert double_linked_list_identical(ans, output)


def test_case2():
    head = construct_double_linked_list([1, 1, 5, 5, 9])
    ans = construct_double_linked_list([1, 1, 5, 9])
    output = Solution.delete_dllnode(head, 5)
    assert double_linked_list_identical(ans, output)


def test_case3():
    head = construct_double_linked_list([1, 1, 5, 5, 9])
    ans = construct_double_linked_list([1, 1, 5, 5, 9])
    output = Solution.delete_dllnode(head, 3)
    assert double_linked_list_identical(ans, output)


def test_case4():
    head = construct_double_linked_list([1, 1, 5, 5, 9])
    ans = construct_double_linked_list([1, 5, 5, 9])
    output = Solution.delete_dllnode(head, 1)
    assert double_linked_list_identical(ans, output)


def test_case5():
    head = construct_double_linked_list([1, 1, 5, 5, 9])
    ans = construct_double_linked_list([1, 1, 5, 5])
    output = Solution.delete_dllnode(head, 9)
    assert double_linked_list_identical(ans, output)