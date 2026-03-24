class Mobile:

    def __init__(self):
        self.name = 'xiaomi'

    def usb_charge(self):
        return 'USB charge.'


class Computer:

    def __init__(self):
        self.name = 'LianXiang'

    def three_charge(self):
        return '3 项插座充电'


class Adapter:

    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


m = Mobile()
c = Computer()
objects = []

objects.append(Adapter(m, charge=m.usb_charge))
objects.append(Adapter(c, charge=c.three_charge))

for obj in objects:
    print(f"{obj.name} begin charge: {obj.charge()}")
