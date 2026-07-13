class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    pass


c1 = MyClass()
c2 = MyClass()

assert c1 is c2
