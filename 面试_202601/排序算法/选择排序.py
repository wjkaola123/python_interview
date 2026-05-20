def select_sort(l):
    length = len(l)
    for i in range(length):

        min_index = i
        for j in range(i + 1, length):
            if l[j] < l[min_index]:
                min_index = j

        l[i], l[min_index] = l[min_index], l[i]


l = [5, 6, 8, 9, 1, 3, 2, 0]
select_sort(l)
print(l)
