class Mixin1(object):
    def test(self):
        print('Mixin1')


class Mixin2(object):
    def test(self):
        print('Mixin2')


class BaseClass:
    def test(self):
        print('BaseClass')


class MyClass(Mixin2, Mixin1, BaseClass):
    def test1(self):
        print('MyClass')


obj = MyClass()
obj.test()
