class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(cls, *args, **kwargs)

        return cls._instance


class A(Singleton):
    pass


a1 = A()
a2 = A()
assert a1 is a2
