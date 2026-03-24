# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        current = head
        if not current:
            return
        le = []
        gte = []
        while current:
            if current.val < x:
                le.append(current)
            else:
                gte.append(current)
            current = current.next
        # rebuild link
        fake_root = cur = ListNode()
        for e in le:
            cur.next = e
            cur = cur.next

        for index, e in enumerate(gte):
            cur.next = e
            cur = cur.next
            if index == len(gte) - 1:
                e.next = None

        return fake_root.next


s = Solution()

n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(5)
n6 = ListNode(2)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

s.partition(n1, 3)
