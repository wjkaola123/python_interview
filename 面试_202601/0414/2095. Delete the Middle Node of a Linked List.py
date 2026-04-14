from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # 求长度
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next

        mid = l // 2
        if mid == 0:
            return None

        cnt = -1
        cur = head
        pre = post = None
        while cur:
            cnt += 1
            if cnt == mid - 1:
                pre = cur
            if cnt == mid + 1:
                post = cur
                break
            cur = cur.next

        if pre:
            pre.next = post
        return head


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
s = Solution()
ret = s.deleteMiddle(n1)
print(ret)
