from collections import deque


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._deque = deque()
        self._min = None

    def push(self, x: int) -> None:
        self._deque.append(x)
        if len(self._deque) == 1:
            self._min = x
        elif x < self._min:
            self._min = x

    def pop(self) -> None:
        pop_num = self._deque.pop()
        if pop_num == self._min and self._deque:
            self._min = min(self._deque)
        return pop_num

    def top(self) -> int:
        if self._deque:
            return self._deque[len(self._deque) - 1]

    def min(self) -> int:
        return self._min
