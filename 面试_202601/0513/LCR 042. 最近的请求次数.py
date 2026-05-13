from collections import deque


class RecentCounter:

    def __init__(self):
        self.deque = deque()

    def ping(self, t: int) -> int:
        self.deque.append(t)
        while self.deque and self.deque[0] < t - 3000:
            self.deque.popleft()
        return len(self.deque)
