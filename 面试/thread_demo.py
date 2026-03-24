import threading
import time


def test(x, y):
    time.sleep(5)
    for i in range(x, y):
        print(i)


# t1 = threading.Thread(target=test, args=(1, 10))
# t1.start()
# t2 = threading.Thread(target=test, args=(11, 20))
# t2.start()


# 自定义线程类
# class MyThread(threading.Thread):
#     def run(self) -> None:
#         print(threading.current_thread().name)
#         for i in range(1, 10):
#             print(i)
#
#
# thread1 = MyThread()
# thread1.start()
# thread1.join(timeout=2)
# thread2 = MyThread()
# thread2.start()

# deamon 属性

t1 = threading.Thread(target=test, args=(1, 10), daemon=True)
t1.start()
data = []
while True:
    time.sleep(2)
    data.append(0)
    print('0 appended to data.')

print('主线程退出')
