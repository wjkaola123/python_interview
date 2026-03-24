import random

s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
result = ''.join(random.sample(s, 7))
print(result)


# 10进制转62进制
def convert(num: int) -> str:
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    res = []
    if num == 0:
        return chars[0]

    while num:
        num, rem = divmod(num, len(chars))
        res.append(chars[rem])

    return ''.join(reversed(res))


print(convert(0))
print(convert(1))
print(convert(61))
print(convert(62))
print(convert(63))
print(convert(64))