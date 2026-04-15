from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break

        return ans


class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n

        for i in range(n):
            if not stack:
                stack.append(i)
                continue

            while stack and temperatures[i] > temperatures[stack[-1]]:
                top_index = stack.pop()
                ans[top_index] = i - top_index

            stack.append(i)

        return ans