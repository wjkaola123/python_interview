from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        path = []

        def dfs(i):
            if len(path) == k:  # path 的长度为k时, 结束递归, 将数据存放到结果数组ans
                ans.append(path.copy())
                return

            for j in range(i, n + 1):  # 选择的范围是[1, n], 所以定义为 [i, n + 1], 并且i从1开始
                path.append(j)  # 加入当前j
                dfs(j + 1)  # 深度优先搜索下一个数
                path.pop()  # 恢复现场

        dfs(1)
        return ans
