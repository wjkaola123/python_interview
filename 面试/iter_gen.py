# iterable = [1, 3, 5, 7, 9]
#
# iterator = iter(iterable)
#
# while True:
#     try:
#         print(next(iterator))
#     except StopIteration as e:
#         print(e.__str__())
#         break


# class MyIterator:
#     def __init__(self):
#         pass
#
#     # def __iter__(self):
#     #     print('__iter__')
#
#     def __next__(self):
#         print('__next__')
#
#
# iterator = MyIterator()
#
# while True:
#     try:
#         next(iterator)
#         break
#     except StopIteration as e:
#         print(e.__str__())
#         break

# generator 生成器

# def my_gen_func():
#     for i in range(10):
#         yield i
#         print('inner:' + str(i))
#
#
# g = my_gen_func()
# while True:
#     try:
#         print('outer:' + str(next(g)))
#     except StopIteration:
#         print('StopIteration')
#         break


def fibonacci(n):
    a, b, counter = 0, 1, 0

    while True:
        if counter <= n:
            yield a
            a, b = b, a + b
            counter += 1
        else:
            return


fb = fibonacci(10)
while True:
    try:
        print(next(fb))
    except StopIteration:
        print('StopIteration')
        break
