import heapq

alist = [5, 7, 9, 1, 3, 2, 5, 4]

heapq.heapify(alist)
s = ''
while alist:
    s += str(heapq.heappop(alist))

print(s)
