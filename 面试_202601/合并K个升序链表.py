import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 用最小堆实现
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists:
            return None

        heap = []
        dummy = current = ListNode(0)
        for head_node in lists:
            while head_node:
                heapq.heappush(heap, head_node.val) # 最小堆实现
                head_node = head_node.next

        while heap:
            value = heapq.heappop(heap)
            node = ListNode(value)
            current.next = node
            current = node

        return dummy.next
