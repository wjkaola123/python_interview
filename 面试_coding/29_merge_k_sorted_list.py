"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 排除链表中为None的元素
        lists = [e for e in lists if e is not None]

        if not lists:
            return None

        first_linkedlist = lists[0]
        if not first_linkedlist and len(lists) == 1:
            return None

        # 提取第一条链表
        head_node = first_linkedlist
        for next_linkedlist in lists[1:]:
            # 后续的链表合并到提取的链表中
            while next_linkedlist:
                # 获取头结点
                current = next_linkedlist
                # next_linkedlist 指针向后移动一个节点
                next_linkedlist = next_linkedlist.next
                # 获取头结点
                current.next = None
                # 将当前节点合并到链表中
                head_node = self.merge_into_linkedlist(current, head_node)

        return head_node


    def merge_into_linkedlist(self, current, head_node):
        # 定义两个指针同时指向第一个和第二个节点
        p1 = head_node
        p2 = head_node.next

        if current.val <= p1.val:
            # 将当前节点插入到链表头部
            current.next = p1
            head_node = current
        else:
            # 当前节点 val > p1.val
            while p2:
                if current.val <= p2.val:
                    current.next = p2
                    p1.next = current
                    break
                else:
                    p1 = p1.next
                    p2 = p2.next

            if p2 is None:
                p1.next = current  # 插入链表的尾部

        return head_node

"""
测试用例1
"""
# n1 = ListNode(1)
# n2 = ListNode(4)
# n3 = ListNode(5)
# n1.next = n2
# n2.next = n3
#
# n4 = ListNode(1)
# n5 = ListNode(3)
# n6 = ListNode(4)
# n4.next = n5
# n5.next = n6
#
# n7 = ListNode(2)
# n8 = ListNode(6)
# n7.next = n8
#
# s = Solution()
# res_head = s.mergeKLists([n1, n4, n7])
# while res_head:
#     print(res_head.val)
#     res_head = res_head.next

"""
测试用例2
"""
n9 = ListNode(1)
s = Solution()
res_head = s.mergeKLists([None, n9])
while res_head:
    print(res_head.val)
    res_head = res_head.next


"""
算法二: 递归算法
"""

class Solution2:
    # 21. 合并两个有序链表
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 用哨兵节点简化代码逻辑
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1  # 把 list1 加到新链表中
                list1 = list1.next
            else:  # 注：相等的情况加哪个节点都是可以的
                cur.next = list2  # 把 list2 加到新链表中
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2  # 拼接剩余链表
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m = len(lists)
        if m == 0:
            return None
        if m == 1:
            return lists[0]  # 无需合并，直接返回
        left = self.mergeKLists(lists[:m // 2])  # 合并左半部分
        right = self.mergeKLists(lists[m // 2:])  # 合并右半部分
        return self.mergeTwoLists(left, right)  # 最后把左半和右半合并