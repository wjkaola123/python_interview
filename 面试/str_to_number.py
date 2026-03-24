a = '1234.569801'

if '.' in a:
    l1 = a.split('.')

num_int = l1[0]
num_float = l1[1]

num_int_list = list(num_int)
num_int_len = len(num_int_list)

num_float_list = list(num_float)
num_float_len = len(num_float_list)

sum = 0
for i in range(num_int_len):
    weight = 10 ** i
    sum += int(num_int_list[num_int_len - 1 - i]) * weight

for i in range(num_float_len):
    quan = -i - 1
    weight = 10 ** quan
    sum += int(num_float_list[i]) * weight

print(sum)
