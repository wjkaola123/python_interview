class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance


class MyClass(Singleton):
    pass


c1 = MyClass()
c2 = MyClass()

assert c1 is c2


# 自定义元类实现单例模式
class MetaClass(type):
    _instance = None

    def __init__(cls, *args, **kwargs):
        cls.name = 'wujie'
        cls.age = 39

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
            cls._instance.__init__(*args, **kwargs)

        return cls._instance


class UserClass(metaclass=MetaClass):
    pass


u1 = UserClass()
u2 = UserClass()

assert u1 is u2
assert u1.name == 'wujie'
assert u1.age == 39
assert u2.name == 'wujie'
assert u2.age == 39


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance


s1 = Singleton()
s2 = Singleton()

assert s1 is s2
