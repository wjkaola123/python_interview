# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        current_a, current_b = headA, headB

        while current_a != current_b:
            current_a = current_a.next if current_a else headB
            current_b = current_b.next if current_b else headA

        return current_a

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        temp = []
        current_a, current_b = headA, headB

        while current_a:
            temp.append(current_a)
            current_a = current_a.next

        while current_b:
            if current_b in temp:
                return current_b
            current_b = current_b.next
