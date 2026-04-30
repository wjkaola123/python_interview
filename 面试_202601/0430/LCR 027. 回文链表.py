from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next

        n = len(l)
        start = 0
        end = n - 1
        while start < end:
            if l[start] == l[end]:
                start += 1
                end -= 1
            else:
                return False

        return True


class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        queue = deque()
        cur = head
        while cur:
            queue.append(cur.val)
            cur = cur.next

        while queue:
            left = queue.popleft()
            # 奇数的情况
            if len(queue) == 0:
                break
            right = queue.pop()
            if left != right:
                return False

        return True


s = Solution2()
n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
assert s.isPalindrome(n1) == False
