def partition(alist, first, last):
    split_value = alist[first]
    leftmark = first + 1
    rightmark = last

    is_done = False
    while not is_done:

        while leftmark <= rightmark and alist[leftmark] <= split_value:
            leftmark += 1

        while rightmark >= leftmark and alist[rightmark] >= split_value:
            rightmark -= 1

        if leftmark > rightmark:
            is_done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark


def quick_sort_helper(alist, first, last):
    if first < last:
        split_index = partition(alist, first, last)
        quick_sort_helper(alist, first, split_index - 1)
        quick_sort_helper(alist, split_index + 1, last)


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist)
    print(alist)
