# Definition for singly-linked list.
from collections import Counter
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        root = cur = ListNode(0)
        current = head
        cnt = Counter()
        while current:
            cnt[current.val] += 1
            current = current.next
        dup = {key for key, val in cnt.items() if val > 1}
        current = head
        while current:
            if current.val not in dup:
                cur.next = ListNode(current.val)
                cur = cur.next
            current = current.next
        return root.next


s = Solution()
head = ListNode(1)
nod2 = ListNode(2)
nod3 = ListNode(2)
head.next = nod2
nod2.next = nod3
s.deleteDuplicates(head)
