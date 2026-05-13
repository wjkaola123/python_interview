class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.alist = []

    def next(self, val: int) -> float:
        self.alist.append(val)
        n = len(self.alist)
        if n <= self.size:
            avg = sum(self.alist) / n
        else:
            start = n - self.size
            avg = sum(self.alist[start:]) / self.size

        return avg
