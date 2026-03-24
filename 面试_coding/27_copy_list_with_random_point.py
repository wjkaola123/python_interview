"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list such that
the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
"""
import collections
from typing import Optional


class Node:
    def __init__(self, x: int, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:

        if not head:
            return head

        current = head
        nodes = []
        new_nodes = []
        while current:
            nodes.append(current)
            new_node = Node(current.val)
            new_nodes.append(new_node)
            current = current.next

        nodes_with_random_index = []
        for node in nodes:
            random_index = nodes.index(node.random) if node.random else None
            nodes_with_random_index.append((node, random_index))

        for i in range(len(new_nodes)):
            random_index = nodes_with_random_index[i][1]
            new_nodes[i].random = new_nodes[random_index] if random_index is not None else None
            if i < len(new_nodes) - 1:
                new_nodes[i].next = new_nodes[i + 1]

        return new_nodes[0]

n1 = Node(7, None, None)
n2 = Node(13, None, None)
n3 = Node(11, None, None)
n4 = Node(10, None, None)
n5 = Node(1, None, None)

n1.next = n2
n1.random = None
n2.next = n3
n2.random = n1
n3.next = n4
n3.random = n5
n4.next = n5
n4.random = n3
n5.next = None
n5.random = n1
node_head = Solution().copyRandomList(n1)

while node_head:
    print(node_head.val)
    node_head = node_head.next
