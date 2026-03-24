"""
# Definition for a Node.
"""
import copy


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        哈希表方法
        :param head:
        :return:
        """
        if not head:
            return None
        current = head
        d = {}
        while current:
            d[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            d[current].next = d.get(current.next)
            d[current].random = d.get(current.random)
            current = current.next

        return d[head]

    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        拼接/拆分法
        :param head:
        :return:
        """
        if not head:
            return None
        current = head
        # 拼接2个的链表 node1 -> newNode1 -> node2 -> newNode2 -> node3 -> newNode3
        while current:
            temp = current.next
            node = Node(current.val)
            current.next = node
            node.next = temp
            current = temp

        current = head
        # 构建新链表各节点的 random 指向
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # 拆分原/新链表
        pre = head
        res = cur = head.next
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None
        return res
