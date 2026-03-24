from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    if not nums:
        return []

    length = len(nums)

    for i in range(length):
        for j in range(length - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


if __name__ == '__main__':
    nums = [8, 4, 9, 1, 3, 10, 6]
    print(bubble_sort(nums))
