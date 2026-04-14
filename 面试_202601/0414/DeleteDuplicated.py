def delete_duplicated(nums):
    n = len(nums)
    i = 0
    while i < n - 1:
        if nums[i] == nums[i + 1]:
            del nums[i]
            n -= 1
        else:
            i += 1


nums = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 9, 10]
delete_duplicated(nums)
print(nums)
