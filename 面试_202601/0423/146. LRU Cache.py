from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._dict = OrderedDict()

    def get(self, key: int) -> int:
        if key in self._dict:
            self._dict.move_to_end(key)
            return self._dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self._dict:
            del self._dict[key]
        else:
            if len(self._dict) >= self._capacity:
                self._dict.popitem(False)
        self._dict[key] = value
