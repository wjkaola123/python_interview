"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""
import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._ordered_dict = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self._ordered_dict:
            self._ordered_dict.move_to_end(key)
            return self._ordered_dict[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._ordered_dict:
            self._ordered_dict.update({key: value})
        else:
            if len(self._ordered_dict) < self.capacity:
                self._ordered_dict[key] = value
            else:
                self._ordered_dict.popitem(last=False)  # 驱逐最不常用的元素
                self._ordered_dict[key] = value

        self._ordered_dict.move_to_end(key)
