"""
协程驱动的函数, 生成器函数
"""


def count(n):
    print("Enter count...")
    while True:
        val = yield n
        n += 1
        print("Val:", val)


c = count(0)
print("获取返回值:", next(c))
res = c.send(100)
print("返回值:", res)
res = c.send(200)
print("返回值:", res)


# for i in range(10):
#     res = c.send(i)
#     print("返回值:", res)


def count_2(n):
    print("Enter count...")
    data = yield n
    yield data


c = count_2(0)
print("获取返回值:", next(c))
res = c.send(100)
print("返回值:", res)

try:
    res = c.send(200)
except StopIteration as e:
    print("返回值:", e.value)