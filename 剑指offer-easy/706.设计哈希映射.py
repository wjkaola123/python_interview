class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    _len = 1009

    @classmethod
    def _h(cls, key):
        return key % cls._len

    def __init__(self):
        self._hashmap = [Node(-1, -1) for _ in range(self._len)]

    def put(self, key: int, value: int) -> None:
        index = self._h(key)
        last_node = head = self._hashmap[index]
        while head:
            if head.key == key:
                break
            last_node = head
            head = head.next

        if head:
            head.value = value
        elif last_node:
            new_nod = Node(key, value)
            last_node.next = new_nod

    def get(self, key: int) -> int:
        index = self._h(key)
        head = self._hashmap[index]
        while head:
            if head.key == key:
                return head.value
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        index = self._h(key)
        pre_node = head = self._hashmap[index]
        while head:
            if head.key == key:
                pre_node.next = head.next
                del head
                break
            pre_node = head
            head = head.next


if __name__ == '__main__':
    m = MyHashMap()
    m.put(1, 2)
    m.put(3, 4)
    m.put(5, 45)
    m.put(6, 46)
    m.put(7, 47)
    m.put(1016, 57)
    # print(m.get(1))
    # print(m.get(3))
    # print(m.get(7))
    # print(m.get(7))
    m.remove(7)
    print(m.get(1016))
