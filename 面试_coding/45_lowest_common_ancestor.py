"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    """
    lowestCommonAncestor 函数的返回值是什么意思？
    答：返回值的准确含义是「最近公共祖先的候选项」。对于最外层的递归调用者来说，返回值是最近公共祖先的意思。
    但是，在递归过程中，返回值可能是最近公共祖先，也可能是空节点（表示子树内没找到任何有用信息）、节点 p 或者节点 q（可能成为最近公共祖先，或者用来辅助判断上面的某个节点是否为最近公共祖先）。
    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 如果当前节点是None, p, q, 直接返回当前节点
        """
        问：为什么发现当前节点是 p 或者 q 就不再往下递归了？万一下面有 q 或者 p 呢？
        答：如果下面有 q 或者 p，那么当前节点就是最近公共祖先，直接返回当前节点。如果下面没有 q 和 p，那既然都没有要找的节点了，也不需要递归，直接返回当前节点。
        """
        if root in (None, p, q):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right: # 左右都找到
            return root # 当前节点是最近公共祖先

        # 如果只有左子树找到，就返回左子树的返回值
        # 如果只有右子树找到，就返回右子树的返回值
        # 如果左右子树都没有找到，就返回 None（注意此时 right = None）
        return left or right
