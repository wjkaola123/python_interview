import functools
import time


def decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        begin = time.time()
        res = func(*args, **kwargs)
        print(f'耗时:{time.time() - begin}')
        return res

    return inner


@decorator
def func(*args, **kwargs):
    time.sleep(args[0])
    return "ok"


if __name__ == '__main__':
    print(func(2))
    # print(func.__name__)