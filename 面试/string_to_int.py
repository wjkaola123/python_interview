a = '1234'

l = list(a)
length = len(l)

sum = 0
for i in range(length):
    weight = 10 ** i
    sum += int(l[length-1-i]) * weight

print(sum)


