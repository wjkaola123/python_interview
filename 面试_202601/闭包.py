import functools
import random
import time


def decorator(func):
    store = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        key = f"{int(begin)}"
        store[key] = end - begin
        print(store)

        return res

    return wrapper


@decorator
def my_sleep():
    time.sleep(random.randint(1, 3))


if __name__ == "__main__":
    for _ in range(5):
        my_sleep()
