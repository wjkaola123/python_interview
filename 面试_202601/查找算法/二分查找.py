def binary_find(nums: list, target: int) -> int:
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return start


print(binary_find([1, 2, 3, 4, 5, 8, 9], 3))
print(binary_find([1, 2, 3, 4, 5, 8, 9, 11, 15, 16, 17], 13))
