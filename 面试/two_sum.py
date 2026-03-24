def two_sum(nums, target):
    d = {}

    for index, num in enumerate(nums):

        other = target - num
        if other in d:
            return index, d[other]
        else:
            d[num] = index

    return None


print(two_sum([9, 1, 2, 7, 11, 15], 9))
