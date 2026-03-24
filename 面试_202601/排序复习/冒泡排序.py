from typing import List


def bubble_sort(nums: List[int]):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


# 测试
print(bubble_sort([3, 2, 1, 4, 5, 6, 7, 8, 9, 10]))
