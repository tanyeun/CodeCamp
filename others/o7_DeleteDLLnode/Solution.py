

class Solution:
    @staticmethod
    def delete_dllnode(head, key):
        if head.val is None:
            return None
        if head.val == key:
            head = head.next
            head.prev = None
            return head
        dummy = head
        while dummy:
            if dummy.val == key:
                if dummy.next is None:
                    dummy.prev.next = None
                else:
                    dummy.prev.next = dummy.next
                    dummy.next.prev = dummy.prev
                return head
            dummy = dummy.next
        return head