# 希尔排序算法
def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]
        position = i
        while position >= gap and current_value < alist[position - gap]:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = current_value


def shellsort(alist):
    sublistcount = len(alist) // 2

    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", alist)
        sublistcount = sublistcount // 2


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shellsort(alist)
