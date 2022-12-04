from typing import Optional
from test.utilities import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
The main trick is 
  head.next = prev
  prev = head
"""
class Solution:
    @staticmethod
    def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            tmp = head.next  # 先把head.next存在tmp
            head.next = prev
            prev = head
            head = tmp       # 再把head指回去

        return prev
