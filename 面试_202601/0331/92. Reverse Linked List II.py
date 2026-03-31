from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return head

        cur = head
        count = 0  # 计数
        middle_head = middle_tail = None # 中段的头尾节点
        pre_connect_node = post_connect_node = None # 中段的头尾连接点

        # 1. 遍历找出上面定义的4个节点
        while cur:
            count += 1
            if count == left - 1:
                pre_connect_node = cur
            if count == left:
                middle_head = cur
            if count == right:
                middle_tail = cur
                post_connect_node = cur.next
            cur = cur.next

        # 2. 从 middle head 到 middle tail进行翻转
        start = middle_head
        end = middle_head.next
        while end and end != post_connect_node:
            next_node = end.next
            end.next = start
            start = end
            end = next_node

        # 3. 连接首部,中部和尾部
        if pre_connect_node:
            pre_connect_node.next = middle_tail
        else:
            head = middle_tail

        if middle_head:
            middle_head.next = post_connect_node

        # 4. 完成局部翻转, 返回头节点
        return head


n1 = ListNode(3)
n2 = ListNode(5)
n1.next = n2
s = Solution()
head = s.reverseBetween(n1, 1, 2)
print(head)
