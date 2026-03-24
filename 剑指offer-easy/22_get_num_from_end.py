class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node_points = []
        current = head
        while current:
            node_points.append(current)
            current = current.next

        return node_points[-k]


if __name__ == '__main__':
    s = Solution()
