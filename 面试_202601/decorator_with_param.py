import time
from functools import wraps


def decorator_outer(second):
    def decorator_inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            time.sleep(second)
            res = func(args, kwargs)
            print(f"spend time: {time.time() - start_time}")
            return res

        return wrapper

    return decorator_inner


@decorator_outer(2)
def hello(*args, **kwargs):
    print("hello")


if __name__ == '__main__':
    hello()
