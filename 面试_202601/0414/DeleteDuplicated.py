def delete_duplicated(nums):
    l1 = []
    for n in nums:
        if n not in l1:
            l1.append(n)

    return l1


nums = [1, 2, 3, 4, 5, 5, 6, 2, 2, 2, 2, 7, 8, 9, 9, 9, 10, 10]
res = delete_duplicated(nums)
print(res)
