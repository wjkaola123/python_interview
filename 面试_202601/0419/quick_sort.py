def partition(alist, left, right):
    povit = alist[left]
    left_mark = left + 1
    right_mark = right
    done = False

    while not done:
        while left_mark <= right_mark and alist[left_mark] < povit:
            left_mark += 1

        while left_mark <= right_mark and alist[right_mark] > povit:
            right_mark -= 1

        if left_mark > right_mark:
            done = True
        else:
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]

    alist[left], alist[right_mark] = alist[right_mark], alist[left]
    return right_mark


def quick_sort_helper(alist, left, right):
    if left < right:
        povit_mark = partition(alist, left, right)
        partition(alist, left, povit_mark - 1)
        partition(alist, povit_mark + 1, right)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort_helper(alist, 0, len(alist) - 1)
assert alist == [17, 26, 20, 31, 44, 54, 55, 77, 93]
