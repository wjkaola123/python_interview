import random


def partition(nums, left, right):
    pivot = nums[left]
    left_mark = left + 1
    right_mark = right

    done = False
    while not done:
        while left_mark <= right_mark and nums[left_mark] <= pivot:
            left_mark += 1

        while right_mark >= left_mark and nums[right_mark] >= pivot:
            right_mark -= 1

        if left_mark > right_mark:
            done = True
        else:
            nums[left_mark], nums[right_mark] = nums[right_mark], nums[left_mark]

    nums[left], nums[right_mark] = nums[right_mark], nums[left]
    return right_mark


def quick_sort_helper(nums, left, right):
    if left < right:
        pivot_position = partition(nums, left, right)
        quick_sort_helper(nums, left, pivot_position - 1)
        quick_sort_helper(nums, pivot_position + 1, right)


nums = [i for i in range(20)]
random.shuffle(nums)
print(nums)
quick_sort_helper(nums, 0, len(nums) - 1)
print(nums)
