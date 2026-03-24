import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._order_dict = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self._order_dict:
            self._order_dict.move_to_end(key)
            return self._order_dict[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._order_dict:
            self._order_dict.update({key: value})
        else:
            if len(self._order_dict) < self.capacity:
                self._order_dict[key] = value
            else:
                self._order_dict.popitem(False)
                self._order_dict[key] = value
        self._order_dict.move_to_end(key)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
