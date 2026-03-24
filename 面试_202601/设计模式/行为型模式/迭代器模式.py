from collections import deque
from typing import Iterable


class Stack(Iterable):

    def __init__(self):
        self._stack = deque()
        self.current = 0

    def push(self, value):
        self._stack.append(value)
        self.current = len(self._stack) - 1

    def pop(self):
        if self._stack:
            value = self._stack.pop()
            self.current = len(self._stack) - 1
            return value
        else:
            raise IndexError

    def peek(self):
        return self._stack[-1]

    def empty(self):
        return len(self._stack) == 0

    def __iter__(self):
        """实现迭代方法__iter__"""
        # res = [item for item in self._stack]
        # res.reverse()
        # for item in res:
        #     yield item
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration("Out of range")

        value = self._stack[self.current]
        self.current -= 1
        return value


# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
#
# for i in s:
#     print(i)
#
# for i in s:
#     print(i)

s1 = Stack()
s1.push(0)
s1.push(8)

it = iter(s1)  # 调用 obj.__iter__()
while True:
    try:
        x = next(it)  # 调用 it.__next__()
        print(x)
    except StopIteration as e:
        print(e)
        break
