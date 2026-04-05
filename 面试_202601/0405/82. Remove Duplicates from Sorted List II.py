from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        end = head.next if head else None
        if start is None or end is None:
            return start

        cur = dummy = ListNode(0)
        d = defaultdict(int)
        d[head.val] += 1
        while end:
            d[end.val] += 1
            if end.val != start.val:
                if d[start.val] == 1:
                    n = ListNode(start.val)
                    cur.next = n
                    cur = cur.next

            start = start.next  # start, end都向前移动一步
            end = end.next

        if d[start.val] == 1:
            cur.next = ListNode(start.val)

        return dummy.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(4)
n7 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

s = Solution()
ret = s.deleteDuplicates(n1)
print(ret)
