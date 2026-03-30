from typing import Optional


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # 利用哈希表保存原节点到新节点的映射关系
        cur = head
        d = {}
        while cur:
            d[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            d[cur].next = d.get(cur.next, None)
            d[cur].random = d.get(cur.random, None)
            cur = cur.next

        return d.get(head, None)
