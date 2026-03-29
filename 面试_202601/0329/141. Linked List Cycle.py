from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 思路: 定义两个指针p1, p2, p1每次走一步, p2每次走两步, 如果两个指针可以重合,说明一定有环;
        # 如果没有环, p1一定无法追上p2.
        if head is None:
            return False

        p1 = head
        p2 = head.next
        while p1 and p2 and p1 != p2:
            p1 = p1.next if p1.next else None
            p2 = p2.next.next if p2.next else None

        return True if p2 else False
