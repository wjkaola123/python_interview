class LowercaseMeta(type):
    """
    修改类的属性名称为小写的元类
    """

    def __new__(mcs, name, bases, attrs):
        lower_attrs = {}
        for k, v in attrs.items():
            if not k.startswith('__'):
                lower_attrs[k.lower()] = v
            else:
                lower_attrs[k] = v

        return type.__new__(mcs, name, bases, lower_attrs)


class LowercaseClass(metaclass=LowercaseMeta):
    BAR = True

    def HELLO(self):
        print('hello')


print(dir(LowercaseClass))
LowercaseClass().hello()
