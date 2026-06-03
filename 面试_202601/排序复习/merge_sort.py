import random


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    res.extend(left if left else right)
    return res


nums = [i for i in range(15)]
random.shuffle(nums)
print(nums)
print(merge_sort(nums))
