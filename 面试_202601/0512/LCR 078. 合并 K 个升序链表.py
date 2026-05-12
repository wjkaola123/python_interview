from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        for node in lists:
            while node:
                h.append(node.val)
                node = node.next

        if not h:
            return None

        heapq.heapify(h)
        root = ListNode(heapq.heappop(h))
        cur = root
        while h:
            n = ListNode(heapq.heappop(h))
            cur.next = n
            cur = cur.next
        return root
