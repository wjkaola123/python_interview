class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        num1 = []
        num2 = []
        while cur1:
            num1.append(str(cur1.val))
            cur1 = cur1.next
        while cur2:
            num2.append(str(cur2.val))
            cur2 = cur2.next

        n1 = int("".join(num1))
        n2 = int("".join(num2))
        n3 = n1 + n2
        num3 = list(str(n3))
        cur = dummy = ListNode(0)
        for n in num3:
            cur.next = ListNode(int(n))
            cur = cur.next

        return dummy.next
