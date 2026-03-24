# 迭代器模式
import functools
from collections import deque


class Stack:

    def __init__(self):
        self._deque = deque()
        self._index = -1

    def push(self, val):
        self._deque.append(val)
        self._index += 1

    def pop(self):
        self._index -= 1
        return self._deque.pop()

    def empty(self):
        return len(self._deque) == 0

    def __iter__(self):
        length = len(self._deque)
        for i in range(length - 1, -1, -1):
            yield self._deque[i]

    def __next__(self):
        if self._index < 0:
            raise StopIteration

        result = self._deque[self._index]
        self._index -= 1

        return result


if __name__ == '__main__':
    s = Stack()
    s.push('a')
    s.push('b')
    s.push('c')

    for item in s:
        print(item)

    print(next(s))
    print(next(s))
    print(next(s))
    # print(next(s))
    print('-' * 50)

    print(list(map(lambda x: x * 2, range(10))))
    sum = functools.reduce(lambda x, y: x + y, (1, 2, 3, 4, 5))
    print(sum)
    print(list(filter(lambda x: x % 2 == 0, range(10))))
