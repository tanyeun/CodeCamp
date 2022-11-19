from typing import Optional
from typing import List
import heapq
from test.utilities import ListNode


class Solution:
    @staticmethod
    def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        list1 = []
        for l1 in lists:
            new_node = l1
            while new_node:
                list1.append(new_node.val)
                new_node = new_node.next

        list1.sort()
        if len(list1) == 0:
            return
        else:
            top = tail = ListNode(list1[0])

            for elements in list1[1:]:
                tail.next = ListNode(elements)
                tail = tail.next

            return top
