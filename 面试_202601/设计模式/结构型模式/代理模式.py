from collections import deque


class Stack:

    def __init__(self):
        self._stack = deque()

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def empty(self):
        return len(self._stack) == 0


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.empty())
