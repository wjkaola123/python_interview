# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        alist = []
        current = head

        while current:
            alist.append(current)
            current = current.next

        if k > len(alist):
            k = k % len(alist)

        if k == 0:  # 不需要翻转
            return alist[0]

        index = len(alist) - k
        pre_index = len(alist) - k - 1
        if pre_index >= 0:
            alist[pre_index].next = None
            alist[len(alist) - 1].next = head
        return alist[index]


if __name__ == '__main__':
    n1 = ListNode(1)
    # n2 = ListNode(2)
    # n3 = ListNode(3)
    # n4 = ListNode(4)
    # n5 = ListNode(5)
    # n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n5
    s = Solution()
    s.rotateRight(n1, 1)
