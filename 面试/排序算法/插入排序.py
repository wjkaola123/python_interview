# 插入排序算法

def insert_sort(l: list) -> list:
    length = len(l)
    for i in range(1, length):
        current_value = l[i]
        position = i

        while position > 0 and current_value < l[position - 1]:
            l[position] = l[position - 1]
            position -= 1

        l[position] = current_value

    return l


if __name__ == '__main__':
    arr = [5, 7, 9, 1, 38, 4, 66, 2]
    print(insert_sort(arr))
