def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i]),


def select_sort(numbers):
    """
    :param numbers:
    :return:
    """
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]


arr = [64, 34, 25, 12, 22, 11, 90]
select_sort(arr)
print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i]),


def insertion_sort(numbers):
    """
    插入排序
    :param numbers:
    :return:
    """
    for i in range(1, len(numbers)):
        currentValue = numbers[i]
        position = i

        while position > 0 and currentValue < numbers[position - 1]:
            numbers[position] = numbers[position - 1]
            position -= 1

        numbers[position] = currentValue


arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i]),
