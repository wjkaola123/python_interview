import random


class RandomizedSet:

    def __init__(self):
        self._s = set()

    def insert(self, val: int) -> bool:
        if val not in self._s:
            self._s.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self._s:
            self._s.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        l = list(self._s)
        n = len(l)
        ind = random.randint(0, n - 1)
        return l[ind]
