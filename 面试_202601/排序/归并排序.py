def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    mid = len(alist) // 2

    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    # 左右两边完成排序, 进行归并
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    # 将left或right 剩余元素加入返回列表
    res.extend(left if left else right)
    return res


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(merge_sort(alist))
