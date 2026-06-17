def dec(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(n)
            res = func(args, kwargs)
            return res

        return wrapper

    return decorator


@dec(10)
def test(*args, **kwargs):
    print("test")


test()
