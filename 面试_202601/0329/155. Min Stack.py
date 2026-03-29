import collections


class MinStack:

    def __init__(self):
        self._min_stack = collections.deque()
        self._min_index = 0

    def push(self, val: int) -> None:
        self._min_stack.append(val)
        if len(self._min_stack) == 1:
            self._min_index = 0
        else:
            # 比较当前入栈值与min_index的值
            if val < self._min_stack[self._min_index]:
                self._min_index = len(self._min_stack) - 1

    def pop(self) -> None:
        min_val = self._min_stack[self._min_index]  # 先取min value
        val = self._min_stack.pop()
        if len(self._min_stack) == 1:
            self._min_index = 0
        else:
            # 判断当前值是否小于栈内所有元素, 重新计算最小值
            if min_val == val and self._min_index >= len(self._min_stack):  # POP 出来的是栈顶的最小值
                # 调整 min index
                self._min_index = len(self._min_stack) - 1
                for index, val in enumerate(self._min_stack):
                    if val < self._min_stack[self._min_index]:
                        self._min_index = index

        return val

    def top(self) -> int:
        return self._min_stack[-1]

    def getMin(self) -> int:
        return self._min_stack[self._min_index]
