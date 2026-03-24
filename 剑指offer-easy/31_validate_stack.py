from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num)  # 入栈
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return not stack


if __name__ == '__main__':
    pass
