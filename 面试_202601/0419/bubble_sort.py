from typing import List


def bubble_sort(nums: List[int]):
    n = len(nums)
    for i in range(n):
        is_exchange = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_exchange = True

        if not is_exchange:
            break


nums = [7, 8, 3, 4, 0, 1, 2]
bubble_sort(nums)
assert nums == [0, 1, 2, 3, 4, 7, 8]
