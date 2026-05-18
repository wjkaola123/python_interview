class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.mini_index = -1

    def push(self, x: int) -> None:
        self.s.append(x)
        if len(self.s) == 1:
            self.mini_index = 0

        if x < self.s[self.mini_index]:
            self.mini_index = len(self.s) - 1

    def pop(self) -> None:
        if self.mini_index == len(self.s) - 1:
            self.s.pop()
            if self.s:
                min_val = min(self.s)
                self.mini_index = self.s.index(min_val)
        else:
            self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.s[self.mini_index]
