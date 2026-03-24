# def foo():
#     print("starting...")
#     i = 100
#     while True:
#         val = yield i
#         print(f'Val:{val}')
#         i += 1
#
#
# g = foo()
# print(next(g))
# # print("*" * 20)
# # print(next(g))
# # print(next(g))
# # print(g.send(99))
#
# for i in range(3):
#     print(f'return: {g.send(i)}')


# 生产者/消费者问题
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('consumer {}'.format(n))
        r = 'ok'


def producer(c):
    n = 0
    while n < 5:
        n += 1
        print('producer {}'.format(n))
        r = c.send(n)
        print('consumer return {}'.format(r))


c = consumer()
next(c)
producer(c)
