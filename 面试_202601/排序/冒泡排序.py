import random
from typing import List


# O(n**2) 的时间复杂度
def bubble_sort(nums: List[int]) -> List[int]:
    length = len(nums)
    for i in range(length):
        for j in range(0, length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

        print(f"第{i}轮:{nums}")

    return nums


# nums = [10, 9, 2, 3, 4, 1]
# print(bubble_sort(nums))

def optimized_bubble_sort(nums: List[int]) -> List[int]:
    length = len(nums)
    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break

    return nums


nums = [i for i in range(30)]
random.shuffle(nums)
print(optimized_bubble_sort(nums))
