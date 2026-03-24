def flist(l=[1]):
    l.append(1)
    print(l)


flist()
flist()

print('*' * 20)


def clear_list(l):
    print(id(l))
    l = []
    print(id(l))


ll = [1, 2, 3]
print(id(ll))
clear_list(ll)
print(ll)
