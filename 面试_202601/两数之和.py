def tow_nums_sum(nums, target):
    d = {}
    for index, num in enumerate(nums):
        other = target - num
        if other in d:
            return index, d[other]
        else:
            d[num] = index
    return None


nums = [3, 5, 2, 4]
print(tow_nums_sum(nums, 8))
