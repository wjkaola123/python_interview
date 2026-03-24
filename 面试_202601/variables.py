class MyClass():
     def __init__(self):
             self.__superprivate = "Hello"
             self._semiprivate = ", world!"

mc = MyClass()
# print(mc.__superprivate)
# print(mc._semiprivate)
# print(mc.__dict__)

# g = (x*x for x in range(10))
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))


class A():
    def foo1(self):
        print("A")
class B(A):
    def foo2(self):
        pass
class C(A):
    def foo1(self):
        print("C")
class D(B, C):
    pass

d = D()
d.foo1()

# A