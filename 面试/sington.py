class Sington():
    instance = None
    list = None

    # def __init__(self):
    #     print('__init__')

    def __new__(cls, *args, **kwargs):
        print('Sington __new__')
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance

    def __call__(self, *args, **kwargs):
        print('__call__')
        pass


# a = Sington()
# b = Sington()
# assert (a == b)
#
# print(id(a))
# print(id(b))


class A(metaclass=Sington):
    a = 100
    b = 200


print('-' * 100)


def work(self):
    print("这是实例方法——————work————————")


Myclass1 = type("Myclass1", (object,), {"a": "100", "b": "200", "work": work})
print(Myclass1)

m = Myclass1()
# m.__dict__['a'] = 300
# m.__dict__['b'] = 400
print(m.a)
print(m.b)
m.work()


# d = {}
# d.update({'a': 1, 'b': 2})
# print(d)
# del d['a']
# print(d)

class Myclass(type):
    """自定义的元类"""

    def __new__(cls, type_name, bases, attrs, *args, **kwargs):
        new_cls = super().__new__(cls, type_name, bases, attrs)
        print("这个是Myclass:", type_name, bases, attrs, )
        return new_cls


class Inherited_class(metaclass=Myclass):
    a = 100
    b = 200


print(type(Inherited_class))

inheritedClass = Inherited_class()
print(inheritedClass.a)
print(inheritedClass.b)
