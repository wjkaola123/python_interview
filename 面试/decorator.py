import time


def time_pay(func):
    def inner(*args, **kwargs):
        for i in range(5):
            time.sleep(1)

        res = func(*args, **kwargs)

        return res

    return inner


@time_pay
def func1(*args, **kwargs):
    print(args)
    print(kwargs)
    print("func1 ...")


l = [1, 2, 3]
d = {"a": 1, "b": 2}
func1(*l, **d)
