class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class ClassA(Singleton):
    pass


c1 = ClassA()
c2 = ClassA()
assert c1 is c2
