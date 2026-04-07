from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        less_point = less_head = ListNode(0)
        greater_point = greater_head = ListNode(0)
        cur = head
        while cur:
            if cur.val < x:
                n = ListNode(cur.val)
                less_point.next = n
                less_point = less_point.next
            else:
                n = ListNode(cur.val)
                greater_point.next = n
                greater_point = greater_point.next
            cur = cur.next

        # 链接两个链表
        if greater_head.next:
            less_point.next = greater_head.next

        return less_head.next


n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(5)
n6 = ListNode(2)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6


def format_linked_nodes(node):
    if not node:
        return "null"
    return f"{node.val} -> {format_linked_nodes(node.next)}"


s = Solution()
ret = s.partition(n1, 3)
print(format_linked_nodes(ret))
