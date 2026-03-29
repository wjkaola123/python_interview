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
    def calculate(self, s: str) -> int:
        stack = Stack()
        operators = ['+', '-']

        for c in s:
            if c == ' ':
                continue
            elif c.isdigit() or c in operators or c == '(':
                stack.push(c)
            elif c == ')':
                target_s = ""
                pop_c = stack.pop()
                while pop_c != "(":
                    target_s = f"{pop_c}{target_s}"
                    pop_c = stack.pop()
                target_num = int(eval(target_s))
                stack.push(target_num)

        target_s = ""
        while not stack.is_empty():
            target_s = f"{stack.pop()}{target_s}"

        return int(eval(target_s))


s = Solution()
assert s.calculate("1 + 1") == 2
assert s.calculate(" 2-1 + 2 ") == 3
assert s.calculate("(1+(4+5+2)-3)+(6+8)") == 23
