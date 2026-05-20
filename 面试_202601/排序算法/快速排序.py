def partition(l, left, right):
    pivot = l[left]
    left_mark = left + 1
    right_mark = right

    done = False
    while not done:
        while left_mark <= right_mark and l[left_mark] < pivot:
            left_mark += 1

        while left_mark <= right_mark and l[right_mark] > pivot:
            right_mark -= 1

        if left_mark > right_mark:
            done = True
        else:
            l[left_mark], l[right_mark] = l[right_mark], l[left_mark]

    l[left], l[right_mark] = l[right_mark], l[left]
    return right_mark


def quick_sort(l, left, right):
    if left < right:
        povit_position = partition(l, left, right)
        quick_sort(l, left, povit_position - 1)
        quick_sort(l, povit_position + 1, right)


l = [7, 9, 8, 4, 6, 2, 3, 1, 5, 0]
quick_sort(l, 0, len(l) - 1)
print(l)
