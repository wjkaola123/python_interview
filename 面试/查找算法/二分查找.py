# 二分查找算法
def binary_find(l: list, target: int) -> int:
    length = len(l)
    start = 0
    end = length - 1
    while start <= end:
        mid = (start + end) // 2
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


if __name__ == '__main__':
    assert binary_find([1, 3, 5, 7, 8, 10, 88], 5) == 2
    assert binary_find([1, 3, 5, 7, 8, 10, 88], 88) == 6
    assert binary_find([1, 3, 5, 7, 8, 10, 88], 11) == -1
