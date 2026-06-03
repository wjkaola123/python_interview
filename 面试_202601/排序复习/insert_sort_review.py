import random


def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        current_value = nums[i]
        position = i
        while position > 0 and nums[position - 1] > current_value:
            nums[position] = nums[position - 1]
            position -= 1

        nums[position] = current_value

    return nums


nums = [i for i in range(15)]
random.shuffle(nums)
print(nums)
print(insert_sort(nums))
