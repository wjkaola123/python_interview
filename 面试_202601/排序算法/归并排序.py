def merge_sort(l):
    if len(l) == 1:
        return l

    mid = len(l) // 2

    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])

    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    res.extend(left if left else right)
    return res


l = [7, 6, 5, 8, 9, 12, 3, 4]

res = merge_sort(l)
print(res)
