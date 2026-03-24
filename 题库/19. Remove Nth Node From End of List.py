# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        alist = []

        if not head or not head.next and n == 1:
            return None

        current = head
        while current:
            alist.append(current)
            current = current.next

        del_index = len(alist) - n
        pre_index = len(alist) - n - 1
        if pre_index >= 0:
            alist[pre_index].next = alist[del_index].next
            del alist[del_index]
        else:
            head = head.next
        return head
