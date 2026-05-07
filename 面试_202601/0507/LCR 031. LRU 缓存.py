from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self._d = OrderedDict()
        self._capacity = capacity

    def get(self, key: int) -> int:
        if key in self._d:
            self._d.move_to_end(key)
            return self._d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self._d:
            del self._d[key]
        else:
            if len(self._d) >= self._capacity:
                self._d.popitem(False)
        self._d[key] = value
