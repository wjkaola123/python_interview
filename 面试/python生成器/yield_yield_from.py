# def chain(*iterables):
#     for it in iterables:
#         for i in it:
#             yield i
#
#
# def chain1(*iterables):
#     for it in iterables:
#         yield from it
#
#
# s = 'ABC'
# t = tuple(range(3))
# print(list(chain1(s, t)))


from collections.abc import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

flatten_list = []
items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    flatten_list.append(x)

print(flatten_list)

print('-' * 20)

flatten_items = []
items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    flatten_items.append(x)

print(flatten_items)
