from collections import deque


class Stack:

    def __init__(self):
        self._s = deque()

    def push(self, val):
        self._s.append(val)

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty.")

        return self._s.pop()

    def is_empty(self):
        return len(self._s) == 0

    def to_string(self):
        return "".join(self._s)


class Solution:
    def removeStars(self, s: str) -> str:
        stack = Stack()
        length = len(s)
        start = 0
        end = length - 1
        ans = []
        while start <= end:
            if s[start] != '*':
                stack.push(s[start])
            else:
                if not stack.is_empty():
                    stack.pop()
            start += 1

        while not stack.is_empty():
            ans.append(stack.pop())
        ans.reverse()
        return "".join(ans)


s = Solution()
assert s.removeStars("leet**cod*e") == "lecoe"
