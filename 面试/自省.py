import datetime
import inspect
import time


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


def is_string(x):
    if isinstance(x, str):
        return True
    else:
        return False


if __name__ == '__main__':
    print(inspect.getmembers(Person, is_string))

    print(inspect.getmodulename(r"C:\Users\wjkao\PycharmProjects\pythonProject\00_two_sum.py"))
    print(inspect.getmodule(Person))

    p = Person('wj', 39)
    print(inspect.ismodule(p))
    print(inspect.isclass(Person))
    print(inspect.ismethod(p.get_name))
    print('*' * 100)
    print(inspect.getsource(Person.get_age))
    # print(inspect.getsourcelines(Person.get_name))
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(dict(zip(['a', 'b'], [1, 2])))
