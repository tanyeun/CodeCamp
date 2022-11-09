from leetcode.l142_LinkedListCycle2.Solution import Solution
from leetcode.l142_LinkedListCycle2.Solution import ListNode


def test_case1():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next = ListNode(-4)
    head.next.next.next = head.next
    output = Solution.detect_cycle(head)
    assert output == head.next


def test_case2():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    output = Solution.detect_cycle(head)
    assert output == head


def test_case3():
    head = ListNode(1)
    output = Solution.detect_cycle(head)
    assert output is None
