from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        if length == 1:
            return head

        k = k % length
        if k == 0:
            return head

        pre_node = point_node = None
        pre_node_index = length - k - 1
        cur = head
        ind = -1
        while cur:
            ind += 1
            if ind == pre_node_index:
                pre_node = cur
            if ind == pre_node_index + 1:
                point_node = cur
                break
            cur = cur.next

        cur = point_node
        if pre_node:
            pre_node.next = None

        while cur and cur.next:
            cur = cur.next

        if cur:
            cur.next = head
        return point_node
