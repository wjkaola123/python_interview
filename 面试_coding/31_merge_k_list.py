from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        merged_list = lists[0]
        for index in range(1, len(lists)):
            merged_list = self.mergeTwoLists(merged_list, lists[index])

        return merged_list



    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        head = current = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                current = l1
                l1 = l1.next
            else:
                current.next = l2
                current = l2
                l2 = l2.next

        current.next = l1 if l1 else l2
        return head.next