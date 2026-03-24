from unittest import result


def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    for x in gen1():
        yield x
"""
不用yield from
"""
g = gen2()
# for x in g:
#     print(x)

"""
使用yield from
"""


def gen3():
    yield from gen1()

g3 = gen3()
# for x in g3:
#     print(x)

# 普通 yield 的局限

def gen():
    yield 1
    yield 2
    return 100

# g = gen()
# res = next(g)
# print(res)  # 50
# g.send(100) # x = 100


def gen4():
    result = yield from gen()
    print("子生成器返回:", result)

# g = gen4()
# print(next(g))   # 1
# print(next(g))   # 2
# next(g)


def sub():
    x = yield 1
    print(f"x={x}")
    y = yield 2
    print(f"y={y}")
    return x + y

def main():
    result = yield from sub()
    print("result =", result)
    yield result

# g = main()
# print(next(g))      # 1
# print(g.send(10))   # 2
#
# try:
#     print(g.send(20))
# except StopIteration as e:
#     print("生成器返回值:", e.value)


def gen_1():
    yield 1
    yield 2
    return 100

def gen_2():
    yield 3
    yield 4
    return 200

def gen_3():
    res = yield from gen_1()
    print(f"res={res}")

g3 = gen_3()
for x in g3:
    print(x)