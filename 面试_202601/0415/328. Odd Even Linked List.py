from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd_head = even_head = None
        odd_cur = None
        even_cur = None
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            if cnt == 1:
                odd_head = ListNode(cur.val)
                odd_cur = odd_head
            if cnt == 2:
                even_head = ListNode(cur.val)
                even_cur = even_head
            if cnt > 1 and cnt % 2 == 1:
                odd_cur.next = ListNode(cur.val)
                odd_cur = odd_cur.next
            elif cnt > 2 and cnt % 2 == 0:
                even_cur.next = ListNode(cur.val)
                even_cur = even_cur.next

            cur = cur.next

        if odd_cur and even_head:
            odd_cur.next = even_head

        return odd_head
