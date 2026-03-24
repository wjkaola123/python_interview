# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head.val == val:
            head = head.next
            return head
        prev = head
        current = head
        while current:
            if current.val == val:
                prev.next = current.next
                break
            else:
                prev = current
                current = current.next
        return head


if __name__ == '__main__':
    s = Solution()
