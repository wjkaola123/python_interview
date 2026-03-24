"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""
import collections
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        node_list1 = []
        node_list2 = []

        current = head
        index = 0
        last_node = None
        while current:
            index += 1
            if index % 2 == 1:
                node_list1.append(current)
            elif index % 2 == 0:
                node_list2.append(current)
            current = current.next

        if len(node_list1) == len(node_list2):
            pairs = [(key, value) for key, value in zip(node_list1, node_list2)]

        if len(node_list1) > len(node_list2):
            last_node = node_list1.pop()
            pairs = [(key, value) for key, value in zip(node_list1, node_list2)]

        # 构建列表
        res_head = current = ListNode()
        for item in pairs:
            current.next = item[1]
            current = item[1].next = item[0]

        if last_node is not None:
            current.next = last_node
        else:
            current.next = None
        return res_head.next

class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        ordered_dict = collections.OrderedDict()

        current = head
        while current and current.next:
            ordered_dict[current.next] = current
            current = current.next.next

        head_node = current_node = ListNode()
        for key, value in ordered_dict.items():
            current_node.next = key
            key.next = value
            current_node = value

        if current:
            current_node.next = current
        else:
            current_node.next = None

        return head_node.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4

s = Solution2()
head = s.swapPairs(n1)

while head:
    print(head.val)
    head = head.next
