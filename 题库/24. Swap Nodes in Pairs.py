# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        current = head
        current_next = head.next

        while current and current_next:
            current.val, current_next.val = current_next.val, current.val
            current = current_next.next
            if current:
                current_next = current.next

        return head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    s = Solution()
    s.swapPairs(node1)

    while node1:
        print(node1.val)
        node1 = node1.next
