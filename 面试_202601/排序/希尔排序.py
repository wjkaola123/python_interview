"""
希尔排序理解为带Gap的多次执行插入排序, 数组从而逐渐变得有序.
Gap值第一次取数组长度的一半, 第二次取第一次的一半, 最终为1
"""


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]
        position = i

        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = current_value


def shellSort(alist):
    gap = len(alist) // 2

    while gap > 0:
        for start_position in range(gap):
            gapInsertionSort(alist, start_position, gap)

        print("After increments of size", gap, "The list is", alist)
        gap = gap // 2  # Gap 每次减半


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shellSort(alist)
    print(alist)
