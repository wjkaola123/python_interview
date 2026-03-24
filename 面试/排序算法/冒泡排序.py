def bubble_sort(l: list) -> list:
    length = len(l)
    for i in range(length):
        for j in range(0, length - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    return l


if __name__ == '__main__':
    print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
