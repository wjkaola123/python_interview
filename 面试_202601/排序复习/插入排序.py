import random


def insert_sort(nums):
    length = len(nums)
    for i in range(1, length):
        current_value = nums[i]
        position = i

        while position > 0 and nums[position - 1] > current_value:
            nums[position] = nums[position - 1]
            position = position - 1

        nums[position] = current_value

    return nums


nums = [i for i in range(30, 50)]
random.shuffle(nums)
print(nums)
print(insert_sort(nums))
