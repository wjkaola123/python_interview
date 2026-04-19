from typing import List


def select_sort(nums: List[int]):
    n = len(nums)
    for i in range(1, n):
        current_value = nums[i]
        position = i

        while position > 0 and nums[i - 1] > current_value:
            nums[i] = nums[i - 1]
            position -= 1
            i -= 1

        nums[position] = current_value


nums = [8, 7, 3, 4, 0, 1, 2]
select_sort(nums)
assert nums == [0, 1, 2, 3, 4, 7, 8]

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
select_sort(alist)
assert alist == [17, 20, 26, 31, 44, 54, 55, 77, 93]
