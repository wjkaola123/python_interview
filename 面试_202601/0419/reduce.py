import time
from functools import reduce

ret = reduce(lambda x, y: x * 2 + y, [1, 2, 3, 4])
print(ret)

print(list(map(lambda x: x ** 2, [0, 1, 2, 3])))


async def fn():
    print("hello")
    return time.time()


obj = fn()
