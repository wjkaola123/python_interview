from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 队列模拟栈操作
        stack = []
        length = len(temperatures)
        res = [0 for _ in range(length)]

        for i in range(length):
            if not stack:
                stack.append(i)
                continue
            while stack and temperatures[i] > temperatures[stack[len(stack) - 1]]:
                top_index = stack.pop()
                res[top_index] = i - top_index
            stack.append(i)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
