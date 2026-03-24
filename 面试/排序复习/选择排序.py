from typing import List


def select_sort(nums: List[int]) -> List[int]:
    if not nums:
        return []

    length = len(nums)

    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if nums[min_index] > nums[j]:
                min_index = j

        nums[min_index], nums[i] = nums[i], nums[min_index]
    return nums


if __name__ == '__main__':
    nums = [8, 4, 9, 1, 3, 10, 6]
    print(select_sort(nums))
