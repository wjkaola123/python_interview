# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        current = head
        tmp = []
        while current:
            tmp.append(current)
            current = current.next
            if current in tmp:
                return True

        return False
