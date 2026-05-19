class Singleton(object):
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


class A(Singleton):
    pass


a1 = A()
a2 = A()
assert a1 is a2
