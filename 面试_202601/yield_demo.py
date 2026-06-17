def count(n):
    print("Enter count...")
    while True:
        value = yield n
        print("val:", value)


c = count(5)
n = next(c)
print("n = ", n)

for i in range(10):
    c.send(i)
