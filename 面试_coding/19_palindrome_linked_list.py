# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        values = []
        reverse_values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        reverse_values[:] = values[::-1]

        if reverse_values == values:
            return True
        else:
            return False

ListNode1 = ListNode(1)
ListNode2 = ListNode(2)
ListNode3 = ListNode(2)
ListNode4 = ListNode(1)
ListNode1.next = ListNode2
ListNode2.next = ListNode3
ListNode3.next = ListNode4

s = Solution()
print(s.isPalindrome(ListNode1))

print("=" * 50)

ListNode5 = ListNode(1)
ListNode6 = ListNode(2)
ListNode5.next = ListNode6
print(s.isPalindrome(ListNode5))