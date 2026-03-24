# Definition for singly-linked list.
from operator import eq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return False
        l1 = []
        while head:
            l1.append(head.val)
            head = head.next
        l2 = l1[::-1]
        if eq(l1, l2):
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    n4 = ListNode(1)
    n3 = ListNode(2, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    print(s.isPalindrome(n1))

    l3 = [1, 2, 3]
    l4 = [1, 2, 3]

    print(l3 == l4)
    print(id(l3))
    print(id(l4))
    print(l3 is l4)
