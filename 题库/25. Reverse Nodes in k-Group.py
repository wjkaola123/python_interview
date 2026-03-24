# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        alist = []
        current = head

        while current:
            alist.append(current)
            current = current.next
        length = len(alist)
        first = 0  # 首指针，指向翻转区间第一个节点
        last = k - 1  # 尾指针，指向翻转区间最后一个节点
        while last < length:
            for i in range(last, first - 1, -1):  # 从区间尾节点向前遍历
                if i == first:  # 遍历到区间第一个节点， 分三种情况进行处理
                    if last + k < length:
                        alist[i].next = alist[last + k]  # 1. 下一个区间最后一个节点在合法范围内，则前一个区间第一个节点的next链接到该节点
                    elif last + 1 < length:
                        alist[i].next = alist[last + 1]  # 2. 说明下一个区间已经超出合法范围，但是 last + 1 仍然在合法范围，将后续剩余节点链接到前一个区间第一个节点上
                    else:
                        alist[i].next = None  # 3. 说明 last + 1已经超出了数组长度， 则将最后一个区间的第一个节点的next设置为None
                else:
                    alist[i].next = alist[i - 1]

            first = first + k  # 向前走k步，进行下一个区间[k, 2k - 1]继续处理
            last = last + k
        return alist[k - 1]  # k-1 是头节点所在位置


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    # node3 = ListNode(3)
    # node4 = ListNode(4)
    # node5 = ListNode(5)
    node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5

    s = Solution()
    s.reverseKGroup(node1, 2)
