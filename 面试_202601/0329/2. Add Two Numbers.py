from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        while l1:
            list1.append(str(l1.val))
            l1 = l1.next

        list2 = []
        while l2:
            list2.append(str(l2.val))
            l2 = l2.next

        list1.reverse()
        list2.reverse()
        num1 = int("".join(list1))
        num2 = int("".join(list2))
        s = num1 + num2
        list3 = list(str(s))
        list3.reverse()
        dummy = cur = ListNode(0)
        for n in list3:
            cur.next = ListNode(int(n))
            cur = cur.next
        return dummy.next






