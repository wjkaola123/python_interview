from collections import Counter


class FreqStack:

    def __init__(self):
        self.stack = []
        self.counter = Counter()

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.counter[val] += 1

    def pop(self) -> int:
        max_frequency = max(self.counter.values())
        for i in range(len(self.stack) - 1, -1, -1):
            if self.counter.get(self.stack[i]) == max_frequency:
                val = self.stack.pop(i)
                self.counter[val] -= 1
                return val


if __name__ == '__main__':
    fs = FreqStack()
    fs.push(5)
    fs.push(7)
    fs.push(7)
    fs.push(7)
    fs.push(7)
    fs.push(5)
    fs.push(5)
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
