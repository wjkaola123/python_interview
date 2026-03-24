from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        for i in range(length):
            for j in range(i + 1, length):
                if temperatures[i] < temperatures[j]:
                    ans[i] = j - i
                    break

        return ans


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))

temperatures = [30, 40, 50, 60]
print(Solution().dailyTemperatures(temperatures))


class Solution2:
    # 单调栈解法
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        stack = []

        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)

        return ans


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution2().dailyTemperatures(temperatures))
