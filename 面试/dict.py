# d = [{'a': 1}, {'a': 1}]
# d2 = {str(item) for item in d}
# d3 = [eval(item) for item in d2]
# print(d3)

# 字典排序
#
# dic = {'a': 18, 'c': 52, 'd': 39}
# print(sorted(dic.items(), key=lambda x: x[1]))

# 列表去重
# l = [0, 1, 1, 2, 2, 3, 4, 5, 5, 7, 9, 77, 77, 79, 79]

# l = list(set(l))
# print(l)

# start = 0
# end = 1
#
# while end <= len(l) - 1:
#     # print(start)
#     # print(end)
#     if l[start] == l[end]:
#         l.pop(end)
#     start += 1
#     end += 1
#
# print(l)

# l = [1, 2, 3, 4]
# print(l.pop())

# 两数之和等于target, 返回（index1, index2）
# def get_two_sum_index(l, target):
#     length = len(l)
#     for i in range(length):
#         for j in range(i + 1, length):
#             if l[i] + l[j] == target:
#                 return i, j
#
#     return -1, -1
#
#
# target = 12
# l = [2, 3, 7, 10]
# print(get_two_sum_index(l, target))

# 字符串转integer

# s = "34897"
# l = list(s)
# length = len(l)
# sum = 0
# for i in range(length):
#     weight = 10 ** (length - 1 - i)
#     sum += int(l[i]) * weight
#
# print(sum)

# 冒泡算法

# l = [9, 8, 7, 6, 1, 2, 3, 4]
# length = len(l)
#
# for i in range(length):
#     for j in range(length - 1 - i):
#         if l[j] > l[j + 1]:
#             l[j], l[j + 1] = l[j + 1], l[j]
#
# print(l)
