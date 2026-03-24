"""
带参数的装饰器
"""
import functools


def dec(param):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("param:", param)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@dec(10)
def test(*args, **kwargs):
    """
    test function
    :param args:
    :param kwargs:
    :return:
    """
    print("test")


print(test.__name__)
print(test.__doc__)
