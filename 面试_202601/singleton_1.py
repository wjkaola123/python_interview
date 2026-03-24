class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self, value):
        self.value = value

c1 = MyClass(1)
c2 = MyClass(2)
print(c1 is c2)  # True
print(c1.value)  # 2
print(c2.value)  # 2