import collections
from typing import List


class Stack:

    def __init__(self):
        self._stack = collections.deque()

    def push(self, val):
        self._stack.append(val)

    def pop(self):
        if len(self._stack) > 0:
            return self._stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self._stack) == 0


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        operators = ['+', '-', '*', '/']
        s = Stack()
        for t in tokens:
            if t not in operators:
                s.push(t)
            else:
                f_num = s.pop()
                s_num = s.pop()
                ans = int(eval(f"{s_num} {t} {f_num}"))
                s.push(ans)
        return s.pop()


s = Solution()
assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
