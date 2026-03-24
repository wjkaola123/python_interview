from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    # 递归结束条件
    if len(nums) <= 1:
        return nums
    middle = len(nums) // 2
    # 减小问题规模
    left = merge_sort(nums[0:middle])
    right = merge_sort(nums[middle:])

    # 合并结果
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    res.extend(left if left else right)
    return res


if __name__ == '__main__':
    lst = [11, 78, 45, 20, 13, 6, 9, 1, 66]
    print(merge_sort(lst))
