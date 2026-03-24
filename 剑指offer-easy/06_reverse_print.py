class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverse_print(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        l1 = []
        current = head
        while current:
            l1.append(current.val)
            current = current.next
        return l1[::-1]


if __name__ == '__main__':
    solution = Solution()
    node3 = ListNode(2)
    node2 = ListNode(3)
    node2.next = node3
    head = ListNode(1)
    head.next = node2
    print(solution.reverse_print(head))
