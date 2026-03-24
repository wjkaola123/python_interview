# 适配器模式

class Computer:

    def __init__(self):
        self.name = '电脑'

    def three_charge(self):
        return '三项插座充电'


class Mobile:

    def __init__(self):
        self.name = '手机'

    def two_charge(self):
        return 'usb 充电'


class Adapter:

    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, item):
        return getattr(self.obj, item)


objects = []

c = Computer()
objects.append(Adapter(c, charge=c.three_charge))

m = Mobile()
objects.append(Adapter(m, charge=m.two_charge))

for obj in objects:
    print(f'{obj.name} 充电方式: {obj.charge()}')
