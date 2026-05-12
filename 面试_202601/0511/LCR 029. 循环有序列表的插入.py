class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        cur = head
        is_find = False
        while not is_find:
            if insertVal >= cur.val and insertVal <= cur.next.val:
                nextnode = cur.next
                cur.next = Node(insertVal)
                cur.next.next = nextnode
                is_find = True
            elif insertVal < cur.val:
                pre = cur
                cur = cur.next
                if cur is cur.next:  # 只有一个节点的case
                    n = Node(insertVal)
                    cur.next = n
                    n.next = cur
                    break

                if cur is head:
                    pre.next = Node(insertVal)
                    pre.next.next = cur
                    break

        return head


n1 = Node(3)
n2 = Node(5)
n3 = Node(1)
n1.next = n2
n2.next = n3
n3.next = n1

s = Solution()
head = s.insert(n1, 3)
print(head)
