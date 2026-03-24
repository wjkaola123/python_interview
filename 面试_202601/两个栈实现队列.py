class MyQueue:

    def __init__(self):
        self.stack_input = []  # 入栈
        self.stack_output = []  # 出栈

    def push(self, x: int) -> None:
        self.stack_input.append(x)

    def pop(self) -> int:
        if self.stack_output:
            return self.stack_output.pop()

        while self.stack_input:
            self.stack_output.append(self.stack_input.pop())
        return self.stack_output.pop()

    def peek(self) -> int:
        if self.stack_output:
            return self.stack_output[-1]

        while self.stack_input:
            self.stack_output.append(self.stack_input.pop())
        return self.stack_output[-1]

    def empty(self) -> bool:
        return len(self.stack_input) == 0 and len(self.stack_output) == 0


queue = MyQueue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.pop()
queue.pop()
queue.push(5)

print(queue.peek())
