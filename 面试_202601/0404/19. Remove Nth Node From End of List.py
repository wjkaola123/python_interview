from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0  # 链表长度
        cur = head
        while cur:
            l += 1
            cur = cur.next

        pre_node = None
        pre_node_ind = l - n - 1

        post_node = None
        post_node_ind = l - n + 1
        ind = -1
        cur = head
        while cur:
            ind += 1
            if ind == pre_node_ind:
                pre_node = cur
            if ind == post_node_ind:
                post_node = cur
            cur = cur.next
        if pre_node and post_node:
            pre_node.next = post_node
        elif pre_node and post_node is None:
            pre_node.next = None
        elif pre_node is None and post_node:
            head = post_node
        elif pre_node is None and post_node is None:
            return None

        return head


head = ListNode(1)
s = Solution()
assert s.removeNthFromEnd(head, 1) is None
