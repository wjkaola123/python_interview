def binary_find(arr, val):
    """
    二分查找
    """
    first, last = 0, len(arr) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == val:
            found = True
            index = mid
        elif arr[mid] > val:
            last = mid - 1
        else:
            first = mid + 1

    return found, index


if __name__ == '__main__':
    arr = [1, 2, 5, 6, 8, 9, 10, 15, 35, 67, 78, 90]
    num = 1
    print(binary_find(arr, num))
