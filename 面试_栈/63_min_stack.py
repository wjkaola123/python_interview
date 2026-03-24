class MinStack:

    def __init__(self):
        self.stack = []
        self.min_index = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_index = 0
            self.stack.append(val)
        elif val <= self.stack[self.min_index]:
            self.stack.append(val)
            self.min_index = len(self.stack) - 1
        elif val > self.stack[self.min_index]:
            self.stack.append(val)

    def pop(self) -> None:
        val_index = len(self.stack) - 1
        self.stack.pop()

        if not self.stack:
            self.min_index = None

        if val_index == self.min_index:
            min_value = min(self.stack)
            self.min_index = self.stack.index(min_value)

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        if self.min_index is not None:
            return self.stack[self.min_index]
        return None


stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.getMin())
stack.pop()
print(stack.top())
print(stack.getMin())
