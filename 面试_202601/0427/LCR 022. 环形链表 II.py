class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        ids = []
        cur = head
        while cur:
            obj_id = id(cur)
            if obj_id not in ids:
                ids.append(obj_id)
            else:
                return cur
            cur = cur.next

        return None
