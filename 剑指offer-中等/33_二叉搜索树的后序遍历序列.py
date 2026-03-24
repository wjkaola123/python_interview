from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:

        current = len(postorder) - 1
        root_val = postorder[current]
        left = []
        right = []
        while current > 0:
            if postorder[current - 1] > root_val:
                right.append(postorder[current - 1])
            elif postorder[current - 1] < root_val:
                left.append(postorder[current - 1])
            current -= 1
