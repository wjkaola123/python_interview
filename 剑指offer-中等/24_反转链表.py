class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        current = head

        while current:
            tmp = current.next
            current.next = pre
            pre = current
            current = tmp

        return pre
