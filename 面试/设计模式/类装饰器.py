import time


class Decorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        begin = time.time()
        res = self.func(*args, **kwargs)
        print(f'耗时:{time.time() - begin}')
        return res


@Decorator
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print("exec func...")
    time.sleep(1)
    return "ok"


if __name__ == '__main__':
    l = ["wj", 39]
    kw = {"a": 1}
    print(type(func))
    res = func(*l, **kw)
    print(res)
