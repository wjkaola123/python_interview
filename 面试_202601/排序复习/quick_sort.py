import random


def partition(alist, left, right):
    pivot = alist[left]
    left_mark = left + 1
    right_mark = right

    done = False
    while not done:
        while left_mark <= right_mark and alist[left_mark] < pivot:
            left_mark += 1

        while left_mark <= right_mark and alist[right_mark] > pivot:
            right_mark -= 1

        if left_mark > right_mark:
            done = True
        else:
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]

    alist[left], alist[right_mark] = alist[right_mark], alist[left]
    return right_mark


def quick_sort_helper(alist, left, right):
    if left < right:
        pivot_position = partition(alist, left, right)
        quick_sort_helper(alist, left, pivot_position - 1)
        quick_sort_helper(alist, pivot_position + 1, right)


nums = [i for i in range(20)]
random.shuffle(nums)
print(nums)

quick_sort_helper(nums, 0, len(nums) - 1)
print(nums)
