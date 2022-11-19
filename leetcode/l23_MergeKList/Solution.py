from typing import Optional
from typing import List
import heapq
from test.utilities import ListNode


# https://leetcode.com/problems/merge-k-sorted-lists/solutions/183195/python-heapq-solution/
class Solution:
    @staticmethod
    def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        pq = []
        for l in lists:
            if l:
                heapq.heappush(pq, l)

        head = node = ListNode()
        while pq:
            node.next = heapq.heappop(pq)
            node = node.next
            if node.next:
                heapq.heappush(pq, node.next)

        return head.next
