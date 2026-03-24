import threading
import dis

n = [0]


def foo():
    # n[0] += 1
    n[0] = n[0] + 1
    n[0] = n[0] + 1
    # n[0] = n[0] + 1


threads = []
for i in range(5000):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

print(n)

# dis.dis(foo)


l = [9, 4, 5, 1, 7, 3]
print(sorted(l, key=lambda x: x))
