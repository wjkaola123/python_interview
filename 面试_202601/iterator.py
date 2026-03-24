from collections import deque
from typing import Iterator, Iterable


class BookShelf:

    def __init__(self):
        self.books = ['西游记', '红楼梦', '三国演义', '水浒传']
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > len(self.books) - 1:
            raise StopIteration()

        data = self.books[self.current_index]
        self.current_index += 1
        return data


bs = BookShelf()
print(isinstance(bs, Iterator))
print(isinstance(bs, Iterable))

for b in bs:
    print(b)
