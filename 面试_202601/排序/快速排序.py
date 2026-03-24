def partition(alist, left, right):
    pivot = alist[left]
    left_mark = left + 1
    right_mark = right

    done = False
    while not done:

        while left_mark <= right_mark and alist[left_mark] <= pivot:
            left_mark += 1

        while left_mark <= right_mark and alist[right_mark] >= pivot:
            right_mark -= 1

        if left_mark > right_mark:
            done = True
        else:
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]

    alist[left], alist[right_mark] = alist[right_mark], alist[left]

    return right_mark


def quick_sort_helper(alist, left, right):
    if left < right:
        pivot_mark = partition(alist, left, right)
        quick_sort_helper(alist, left, pivot_mark - 1)
        quick_sort_helper(alist, pivot_mark + 1, right)

    return alist


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort_helper(alist, 0, len(alist) - 1)
    print(alist)
