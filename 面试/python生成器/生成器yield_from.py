# def generator1():
#     for i in range(5):
#         yield i
#
#
# def generator2():
#     yield 'a'
#     yield 'b'
#     yield 'c'
#     yield from generator1()
#     yield from [10, 11, 12, 13]
#     yield from [12, 13, 14]
#     yield from range(3)


# for i in generator2():
#     print(i, end=",")


def my_generator():
    for i in range(5):
        if i == 2:
            return '我被迫中断了'
        else:
            yield i


def yield_from_wrap(g):
    result = yield from g
    yield result # 返回"我被迫中断了"


def main(generator):
    # try:
    for i in generator:
        print(i, end=',')


# except StopIteration as e:
#     print('*' * 10)
#     print(e.value)

g = my_generator()  # 子生产器
wrap_g = yield_from_wrap(g)  # 委派生产器
main(wrap_g)  # 调用方



