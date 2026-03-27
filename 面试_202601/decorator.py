import time
from functools import wraps


def time_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()

        print(f"函数执行时间: {round(end_time - start_time, 2)} seconds.")
        return res

    return wrapper



@time_decorator
def demo():
    """I'm the demo function."""
    for i in range(1, 6):
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    print(demo.__name__)
    print(demo.__doc__)
    print(demo.__module__)
    print(demo.__wrapped__)

    demo()
