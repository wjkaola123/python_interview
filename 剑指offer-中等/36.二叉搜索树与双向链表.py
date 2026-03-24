"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        alist = []

        def enorder_traversal(root: Node):
            if not root:
                return
            if root.left:
                enorder_traversal(root.left)
            alist.append(root)
            if root.right:
                enorder_traversal(root.right)

        enorder_traversal(root)

        if len(alist) == 1:
            alist[0].left = alist[0]
            alist[0].right = alist[0]
        elif len(alist) > 1:
            for i in range(len(alist)):
                if i == 0:
                    alist[i].right = alist[i + 1]
                    alist[i].left = alist[len(alist) - 1]
                elif i == len(alist) - 1:
                    alist[i].right = alist[0]
                    alist[i].left = alist[i - 1]
                else:
                    alist[i].right = alist[i + 1]
                    alist[i].left = alist[i - 1]
        return alist[0]


if __name__ == '__main__':
    # node5 = Node(5)
    # node4 = Node(4)
    # node3 = Node(3)
    # node2 = Node(2)
    node1 = Node(1)
    # node2.left = node1
    # node2.right = node3
    # node4.left = node2
    # node4.right = node5
    s = Solution()
    node = s.treeToDoublyList(node1)
    print(node.val)
