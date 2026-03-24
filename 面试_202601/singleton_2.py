def singleton(cls):
    """A decorator to make a class a Singleton."""
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class MyClass:
    def __init__(self, value):
        self.value = value

@singleton
class MyClass2:
    def __init__(self, value):
        self.value = value


c1 = MyClass(1)
c2 = MyClass(2)
c3 = MyClass2(3)
print(c1 is c2)  # True
print(c1.value)  # 1
print(c2.value)  # 1
print(c3.value)  # 3
print(c1 is c3)  # False
