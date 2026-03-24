# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current = node
        next_node = node.next

        while next_node:
            current.val = next_node.val
            pre_node = current
            current = next_node
            next_node = current.next

        pre_node.next = None
