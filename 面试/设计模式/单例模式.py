class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    pass


c1 = MyClass()
c2 = MyClass()
print(id(c1))
print(id(c2))

assert c1 is c2
