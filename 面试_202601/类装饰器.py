import functools
import time

"""
类装饰器,支持传递参数
"""


class LogTime:

    def __init__(self, use_int: bool = False):
        self.use_int = use_int

    def __call__(self, func):
        @functools.wraps(func)
        def _log(*args, **kwargs):
            begin = time.time()
            print("Args: {}".format(args))
            res = func(*args, **kwargs)

            if self.use_int:
                print("Use time: {}".format(
                    int(time.time() - begin))
                )
            else:
                print("Use time: {}".format(
                    time.time() - begin
                ))

            return res

        return _log


@LogTime(True)
def my_sleep(a, b):
    """
    :param a:  add number
    :param b:  add number
    :return:   result
    """
    time.sleep(1)
    return a + b


print(my_sleep.__name__)
print(my_sleep.__doc__)
print(my_sleep.__dict__)
print(dir(my_sleep))
print(my_sleep(10, 20))
