# Definition for singly-linked list.
from typing import List, Optional
from heapq import heapify, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        temp_list = []
        for item in lists:
            while item:
                temp_list.append(item.val)
                item = item.next

        if not temp_list:
            return None
        heapify(temp_list)
        root = ListNode(heappop(temp_list))
        current_node = root
        while temp_list:
            next_node = ListNode(heappop(temp_list))
            current_node.next = next_node
            current_node = next_node
        return root

    def mergeTwoList(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged = ListNode(0)
        current = merged
        while l1 and l2:
            if l1.val < l2.val:
                current_node = ListNode(l1.val)
                l1 = l1.next
            else:
                current_node = ListNode(l2.val)
                l2 = l2.next

            current.next = current_node
            current = current.next

        current.next = l1 if l1 else l2

        return merged.next

    # 合并多个有序链表
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        merged = lists[0]
        for index, node in enumerate(lists):
            if index > 0:
                merged = self.mergeTwoList(merged, node)

        return merged


if __name__ == '__main__':
    s = Solution()

    temp = [3, 2, 6, 9, 5, 8, 7, 1]
    heapify(temp)
    while temp:
        print(heappop(temp))
