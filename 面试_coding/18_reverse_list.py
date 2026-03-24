from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        pre = ListNode(None)
        pre.next = head
        current = head
        suf = current.next

        while current:
            current.next = pre
            if suf is not None:
                pre = current
                current = suf
                suf = suf.next
            else:
                break
        head.next = None
        return current



ListNode1 = ListNode(1)
ListNode2 = ListNode(2)
ListNode3 = ListNode(3)
ListNode4 = ListNode(4)
ListNode5 = ListNode(5)
ListNode1.next = ListNode2
ListNode2.next = ListNode3
ListNode3.next = ListNode4
ListNode4.next = ListNode5

head = ListNode1
# while head:
#     print(head.val)
#     head = head.next
#
# print('=' * 20)

s = Solution()
reversed_head = s.reverseList(head)
while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next
