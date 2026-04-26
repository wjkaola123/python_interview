from functools import wraps


def singleton(cls):
    instance = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper


@singleton
class A:
    pass


a1 = A()
a2 = A()

assert a1 is a2
