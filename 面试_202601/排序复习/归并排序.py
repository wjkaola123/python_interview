def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    mid = len(alist) // 2

    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    res.extend(left if left else right)
    return res


alist = [50, 31, 22, 4, 5, 89, 19, 10, 9]
print(merge_sort(alist))
