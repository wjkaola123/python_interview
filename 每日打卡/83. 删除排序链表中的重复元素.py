# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        current = head
        current_next = current.next
        while current:
            while current_next and current_next.val == current.val:
                current_next = current_next.next
            current.next = current_next
            current = current.next

        return head


s = Solution()
n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(1)
n1.next = n2
n2.next = n3

s.deleteDuplicates(n1)
