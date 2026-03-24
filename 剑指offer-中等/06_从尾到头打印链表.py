# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.reverse()
        return l


if __name__ == '__main__':
    node2 = ListNode(2)
    node3 = ListNode(3)
    node3.next = node2
    node1 = ListNode(1)
    node1.next = node3

    s = Solution()
    print(s.reversePrint(node1))
