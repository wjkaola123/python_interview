funcs = []
for i in range(3):
    def f():
        return i


    funcs.append(f)

print([f() for f in funcs])

funcs = []
for i in range(3):
    def f(i=i):
        return i


    funcs.append(f)

print([f() for f in funcs])  # [0, 1, 2]


def make_func(i):
    def f():
        return i

    return f


funcs = [make_func(i) for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2]

def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = counter()
print(c())  # 1
print(c())  # 2


def deco(func):
    print("A")
    def wrapper():
        print("B")
        func()
        print("C")
    return wrapper

@deco
def foo():
    print("D")

foo()

#################################################

def deco(func):
    def wrapper():
        print(i)
        func()
    return wrapper

funcs = []
for i in range(3):
    @deco
    def f():
        print("hello")
    funcs.append(f)

for f in funcs:
    f()

