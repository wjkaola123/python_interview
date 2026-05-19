import time
from functools import wraps


def decorator_outer(second):
    def decorator_inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            time.sleep(second)
            res = func(*args, **kwargs)
            print(f"spend time: {time.time() - start_time}")
            return res

        return wrapper

    return decorator_inner


@decorator_outer(1)
def hello(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(key, value)


if __name__ == '__main__':
    hello(1, 2, 'a', c=0, d=1)
