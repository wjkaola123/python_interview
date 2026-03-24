class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 找p节点经过的路径
        p_path = self.find_path(p, root)
        # 找q节点经过的路径
        q_path = self.find_path(q, root)
        ancestor = None
        for u, v in zip(p_path, q_path):
            if u == v:
                ancestor = u
            else:
                break
        return ancestor

    def find_path(self, target, root):
        path = []
        current = root
        while current != target:
            path.append(current)
            if current.val < target.val:
                current = current.right
            else:
                current = current.left
        path.append(current)
        return path


if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    for item in zip(list1, list2):
        print(item)
