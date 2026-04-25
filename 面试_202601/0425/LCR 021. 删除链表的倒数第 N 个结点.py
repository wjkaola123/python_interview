class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head

        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        ind = length - n
        cnt = -1
        cur = head
        pre_node = None
        next_node = None
        while cur:
            cnt += 1
            if cnt == ind - 1:
                pre_node = cur
            if cnt == ind:
                next_node = cur.next
            cur = cur.next

        if pre_node and next_node:
            pre_node.next = next_node
        elif pre_node and not next_node:
            pre_node.next = None
        elif not pre_node:
            head = head.next

        return head
