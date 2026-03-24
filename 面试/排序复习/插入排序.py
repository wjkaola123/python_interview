from typing import List


def insert_sort(nums: List[int]) -> List[int]:
    if not nums:
        return []

    for i in range(1, len(nums)):
        current_value = nums[i]
        position = i
        while position > 0 and nums[position - 1] > current_value:
            nums[position] = nums[position - 1]
            position -= 1

        nums[position] = current_value

    return nums


if __name__ == '__main__':
    nums = [8, 4, 9, 1, 3, 10, 6]
    print(insert_sort(nums))
