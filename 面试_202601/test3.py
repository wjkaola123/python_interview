from functools import reduce

res = map(lambda x: x * 2, [1, 2, 3])
print(list(res))

res = reduce(lambda x, y: x + y, [0, 1, 2, 10, 20])
print(res)

print(sorted([8, 4, 5, 1, 2, 4, 3]))

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]
res = zip(l1, l2)
print(list(res))

l3 = [0, 2, 4, 5, 7, 8]
print(list(filter(lambda x: x%2 == 0, l3)))
