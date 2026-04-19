from functools import reduce

ret = reduce(lambda x, y: x * 2 + y, [1, 2, 3, 4])
print(ret)
