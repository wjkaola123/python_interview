from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        n = 0
        cur = head
        # 1.算出链表的长度
        while cur:
            n += 1
            cur = cur.next

        # 2.算出有几个分组
        times = n // k
        start = head
        end = head.next
        dummy = cur = ListNode(0)  # 假头节点
        # 3. 按分组进行迭代, 翻转后的局部链表加入头节点
        for _ in range(times):
            c = 0
            first_node = None
            while c < k - 1:  # 一轮翻转
                next_node = end.next
                end.next = start
                if c == 0:
                    first_node = start  # 保存每轮第一个节点
                    start.next = None  # 每轮第一个节点的next指向空
                start = end
                end = next_node
                c += 1

            cur.next = start  # 翻转的局部链表加入头节点
            cur = first_node  # 移动到末端节点, 以便新的分组加入
            # 指针移动到下个分组的前两个元素
            start = end
            end = end.next if end else None

        # 把未分组的数据加入链表中
        cur.next = start if start else None
        return dummy.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

s = Solution()
ret = s.reverseKGroup(n1, 2)
print(ret)
