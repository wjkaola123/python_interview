import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"params: {args[0]}, {args[1]}")
        return func(*args, **kwargs)

    return wrapper


@decorator
def func(a, b):
    return a + b


ret = func(1, 2)
print(ret)
