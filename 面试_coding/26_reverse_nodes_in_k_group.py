"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        sorted_nodes = []
        left_nodes_num = n % k # 剩余的节点数
        times = n // k # 指针移动的次数
        current = head
        for i in range(times):
            nodes = []
            for j in range(k):
                nodes.append(current)
                current = current.next
            nodes.reverse()
            sorted_nodes.extend(nodes)

        if left_nodes_num > 0:
            for _ in range(left_nodes_num):
                sorted_nodes.append(current)
                current = current.next
        else:
            sorted_nodes[-1].next = None

        head_node = current = ListNode()
        for node in sorted_nodes:
            current.next = node
            current = node

        return head_node.next

n1 = ListNode(1)
n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)

n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

s = Solution()
head_node = s.reverseKGroup(n1, 2)
while head_node:
    print(head_node.val)
    head_node = head_node.next