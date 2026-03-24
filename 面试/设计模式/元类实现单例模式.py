class Singleton(type):

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance


class MyClass(metaclass=Singleton):
    pass


c1 = MyClass()
c2 = MyClass()

assert c1 is c2
