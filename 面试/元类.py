class FirstMetaClass(type):

    # cls代表动态修改的类
    # name代表动态修改的类名
    # bases代表被动态修改的类的所有父类
    # attr代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        attrs['name'] = 'wujie'
        attrs['say'] = lambda self: print(f"call say(): {attrs['name']} 实例方法")

        return super().__new__(cls, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print("调用元类__call__方法")

        i = cls.__new__(cls)
        i.__init__(*args, **kwargs)
        return i


class Clanguage(object, metaclass=FirstMetaClass):
    pass


clangs = Clanguage()
print(clangs.name)
clangs.say()
