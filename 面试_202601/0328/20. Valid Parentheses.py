# 考虑使用栈来解决
import collections


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
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False

        stack = Stack()  # 队列模拟栈
        d = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in ['(', '{', '[']:
                stack.push(c)
            else:
                if d[c] != stack.pop():
                    return False

        return stack.is_empty()
