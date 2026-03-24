class Person:

    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, num):
        if num >= 18:
            self.__age = num
        else:
            raise ValueError('Age below 18 is not possible.')

    @age.deleter
    def age(self):  # 由于这里的方法名为age，所以要删除属性，需要使用age
        print('删除age属性')
        del self.__age


if __name__ == '__main__':
    person = Person()
    age = person.age
    print(age)

    # 添加修改属性的方式，可以通过 @属性名.setter 方式来完成
    person.age = 18
    print(person.age)

    del person.age
