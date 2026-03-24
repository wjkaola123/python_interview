from flatbuffers.flexbuffers import Object


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance


class ClassA(Singleton):
    pass


a1 = ClassA()
a2 = ClassA()
assert a1 is a2
