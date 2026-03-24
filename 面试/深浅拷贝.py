import copy
from threading import Lock

l1 = [[1, 2], (4, 5), [3, {"a": [6, 7]}]]
l2 = copy.deepcopy(l1)

print(id(l1))
print(id(l2))

print('*' * 10 + " 深拷贝 " + '*' * 10)
print('比较第一个元素（可变对象）:')
print(id(l1[0]), id(l2[0]))

print('比较第二个元素（不可变对象）:')
print(id(l1[1]), id(l2[1]))

print('比较第三个元素（可变对象）:')
print('常量:')
print(id(list(l1[2][1].keys())[0]), id(list(l2[2][1].keys())[0]))
print('变量:')
print(id(l1[2][1]["a"]), id(l2[2][1]["a"]))

print('*' * 10 + " 浅拷贝 " + '*' * 10)
# 浅拷贝
l3 = copy.copy(l1)

print(id(l1))
print(id(l3))
print('比较第一个元素（可变对象）:')
print(id(l1[0]), id(l3[0]))

main