class Person:

    def __init__(self):
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, num):
        if num >= 18:
            self.__age = num
        else:
            raise ValueError('Age below 18 is not possible.')

    def del_age(self):
        print('将要删除age属性')
        del self.__age

    age = property(get_age, set_age, del_age)


if __name__ == '__main__':
    person = Person()
    print(person.age)

    person.age = 19
    print(person.age)
    del person.age
