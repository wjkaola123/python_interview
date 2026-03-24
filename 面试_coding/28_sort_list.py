"""
Given the head of a linked list, return the list after sorting it in ascending order.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        head_node = ListNode(val=-99999)
        current = head
        index = 0
        while current:
            is_linked = False
            if index == 0:
                head_node.next = ListNode(val=current.val) # 将第一个节点挂入新链表中
                is_linked = True
            else:
                # 将当前节点依次与新链表中的每一个元素进行比较
                while p2:
                    if p1.val <= current.val <= p2.val:
                        n = ListNode(val=current.val)
                        p1.next = n
                        n.next = p2
                        is_linked = True
                        break
                    else:
                        # 当前节点值大于p2节点时, 继续向后查找
                        p1 = p1.next
                        p2 = p2.next

            if not is_linked:
                n = ListNode(val=current.val)
                p1.next = n # 将节点链入到队列尾部

            p1 = head_node
            p2 = head_node.next
            current = current.next
            index += 1

        return head_node.next

"""
方法二: 
1. 将值存入列表
2. 对列表排序
3. 将排序后的列表元素依次更新到队里中  
"""
class Solution2:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        current = head
        while current:
            list1.append(current.val)
            current = current.next

        sorted_list = sorted(list1)
        current = head
        for index in range(len(sorted_list)):
            current.val = sorted_list[index]
            current = current.next

        return head

n1 = ListNode(4)
n2 = ListNode(2)
n3 = ListNode(1)
n4 = ListNode(3)

n1.next = n2
n2.next = n3
n3.next = n4

s = Solution2()
head = s.sortList(n1)
print(head)