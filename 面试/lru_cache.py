from collections import OrderedDict


class LruCache:

    def __init__(self, capacity: int):
        self.order_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.order_dict:
            return -1
        else:
            value = self.order_dict.get(key)
            self.order_dict.move_to_end(key)
            return value

    def put(self, key, value):
        if len(self.order_dict) >= self.capacity:
            if key in self.order_dict:
                self.order_dict.pop(key)
            else:
                self.order_dict.popitem(False)
        self.order_dict.update({key: value})


if __name__ == '__main__':
    lru_cache = LruCache(3)

    lru_cache.put("a", 1)
    lru_cache.put("b", 2)
    lru_cache.put("c", 3)

    print(lru_cache.order_dict)

    lru_cache.put("d", 4)
    lru_cache.put("e", 5)

    print(lru_cache.order_dict)
    print(lru_cache.get("d"))
    print(lru_cache.order_dict)

    lru_cache.put("c", 30)
    print(lru_cache.order_dict)
