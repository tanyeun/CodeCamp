from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:    #Cycle detected
                fast = head
                while fast is not slow:
                    fast = fast.next
                    slow = slow.next
                return fast
