# 可迭代对象（list、tuple、str、dict、set 等）
my_list = [1, 2, 3, 4, 5]
my_str = "hello"

# 转换为迭代器
list_iterator = iter(my_list)
str_iterator = iter(my_str)

print(type(list_iterator))  # <class 'list_iterator'>
print(next(list_iterator))  # 1
print(next(list_iterator))  # 2

# 2. 迭代器 → 可迭代对象：不需要转换！
# 创建一个迭代器
my_list = [1, 2, 3]
iterator = iter(my_list)

# 迭代器可以直接用在 for 循环中
for item in iterator:
    print(item)  # 输出: 1, 2, 3

# 也可以转换为列表（消耗迭代器）
iterator2 = iter([1, 2, 3])
new_list = list(iterator2)  # [1, 2, 3]
print(new_list)

# 迭代器是一次性的
numbers = [1, 2, 3]
iterator = iter(numbers)

# 第一次遍历
print(list(iterator))  # [1, 2, 3]

# 第二次遍历（迭代器已耗尽）
print(list(iterator))  # []  空列表！

# 判断是否为迭代器
from collections.abc import Iterator, Iterable

my_list = [1, 2, 3]
iterator = iter(my_list)

print(isinstance(my_list, Iterable))   # True
print(isinstance(my_list, Iterator))   # False

print(isinstance(iterator, Iterable))  # True
print(isinstance(iterator, Iterator))  # True
