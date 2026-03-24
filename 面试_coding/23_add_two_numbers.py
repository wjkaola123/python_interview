"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = ""
        l2_str = ""
        head = current = None

        while l1:
            l1_str += str(l1.val)
            l1 = l1.next

        while l2:
            l2_str += str(l2.val)
            l2 = l2.next

        num1 = int(l1_str[::-1])
        num2 = int(l2_str[::-1])
        num3 = num1 + num2

        num3_list = list(str(num3))
        num3_list.reverse()

        for index, num3 in enumerate(num3_list):
            if index == 0:
                head = current = ListNode(int(num3))
            else:
                current.next = ListNode(int(num3))
                current = current.next

        return head

n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(3)

n1.next = n2
n2.next = n3

n4 = ListNode(5)
n5 = ListNode(6)
n6 = ListNode(4)
n4.next = n5
n5.next = n6

s = Solution()
head = s.addTwoNumbers(n1, n4)
while head:
    print(head.val)
    head = head.next
