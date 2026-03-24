def send_to_generator():
    i = -1
    while True:
        i += 1
        result = yield i
        print(result)


c = send_to_generator()
res = next(c)
print('第一个返回值:{}'.format(res))
for i in range(10):
    data = f"发送值:ok{i}"
    r = c.send(data)
    print(f"返回值:{r}")
