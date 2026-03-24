"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        current = head
        steps = length - n - 1
        if steps > 0:
            for _ in range(steps):
                current = current.next
        elif steps == -1:
            head = head.next

        if current.next:
            current.next = current.next.next

        return head


node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2

s = Solution()
head = s.removeNthFromEnd(node1, 1)
print(head.val)