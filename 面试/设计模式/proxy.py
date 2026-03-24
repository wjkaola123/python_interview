# 代理模式
from collections import deque


class Stack:

    def __init__(self):
        self._deque = deque()

    def push(self, val):
        self._deque.append(val)

    def pop(self):
        return self._deque.pop()

    def empty(self):
        return len(self._deque) == 0


if __name__ == '__main__':
    s = Stack()
    s.push('a')
    s.push('b')
    s.push('c')

    print(s.pop())
    print(s.pop())
    print(s.pop())

    print(s.empty())
