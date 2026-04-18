from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        d = defaultdict(int)
        n = 0
        max_sum = 0
        while cur:
            n += 1
            cur = cur.next

        cur = head
        i = 0
        while cur:
            key = tuple(sorted([i, n - 1 - i]))
            if i in key:
                d[key] += cur.val
                max_sum = max(max_sum, d[key])
            cur = cur.next
            i += 1

        return max_sum


n1 = ListNode(5)
n2 = ListNode(4)
n3 = ListNode(2)
n4 = ListNode(1)
n1.next = n2
n2.next = n3
n3.next = n4
s = Solution()
assert s.pairSum(n1) == 6
