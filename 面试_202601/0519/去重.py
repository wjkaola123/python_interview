def remove_duplicated(alist):
    alist2 = []
    for n in alist:
        if n not in alist2:
            alist2.append(n)
    return alist2


alist = [1, 1, 5, 6, 5, 5, 8, 7, 7, 9]

alist2 = remove_duplicated(alist)
print(alist2)
