import random


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]
        position = i

        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = current_value


def shell_sort(alist):
    gap = len(alist) // 2

    while gap > 0:
        for start in range(gap):
            gapInsertionSort(alist, start, gap)

        gap = gap // 2


nums = [i for i in range(10, 25)]
random.shuffle(nums)
print(nums)
shell_sort(nums)
print(nums)
