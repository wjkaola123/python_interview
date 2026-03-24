from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return

            for j in range(i, n):
                c = s[i:j + 1] # 从第i个位置开始, 逐个向后截取子串
                if c == c[::-1]: # 判断是否为回文
                    path.append(c)
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return ans


s = Solution()
ans = s.partition('aab')
print(ans)
