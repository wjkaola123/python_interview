# 选择排序
def select_sort(l: list) -> list:
    length = len(l)

    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if l[j] < l[min_index]:
                min_index = j

        l[i], l[min_index] = l[min_index], l[i]

    return l


if __name__ == '__main__':
    print(select_sort([64, 34, 25, 12, 22, 11, 90]))
