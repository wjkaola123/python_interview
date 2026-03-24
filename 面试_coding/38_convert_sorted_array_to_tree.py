"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(nums, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    node = TreeNode(nums[mid])

    node.left = dfs(nums, start, mid - 1)
    node.right = dfs(nums, mid + 1, end)

    return node

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return dfs(nums, 0, len(nums) - 1)