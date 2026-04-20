class A:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # Support modify name
    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age


a = A("Jie", 43)
assert a._name == 'Jie'
assert a.name == 'Jie'
assert a.age == 43

a.name = "Jack"
a.age = 28
assert a.name == 'Jack'
assert a.age == 28
