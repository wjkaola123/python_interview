import threading
import time

# class MyThread(threading.Thread):
#
#     def run(self) -> None:
#         global x
#         lock.acquire()
#         x += 10
#         print('{}:{}'.format(self.name, x))
#         lock.release()
#
#
# x = 0
# lock = threading.RLock()
# for i in range(10):
#     t = MyThread()
#     t.start()


# 同步锁/可重入锁
# num = 0
#
#
# def add():
#     with lock:
#         global num
#         for i in range(10000000):
#             num += 1
#
#
# def sub():
#     with lock:
#         global num
#         for i in range(10000000):
#             num -= 1
#
#
# lock = threading.RLock()
#
# t1 = threading.Thread(target=add)
# t2 = threading.Thread(target=sub)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print(f"num:{num}")

# 条件锁
# currentRunThreadNumber = 0
# maxSubThreadNumber = 10
#
#
# def task():
#     global currentRunThreadNumber
#     thName = threading.current_thread().name
#
#     with condLock:
#         print('start and wait run thread : %s' % thName)
#         condLock.wait()
#         currentRunThreadNumber += 1
#         print('carry on run thread : %s' % thName)
#
#
# if __name__ == '__main__':
#     condLock = threading.Condition()
#     for i in range(maxSubThreadNumber):
#         subThreadIns = threading.Thread(target=task)
#         subThreadIns.start()
#
#     while currentRunThreadNumber < maxSubThreadNumber:
#         notifyNumber = int(
#             input('Please enter the number of threads that need to be notified to run: '))
#         with condLock:
#             condLock.notify(notifyNumber)
#
#     print('main thread run end')

# Event() 事件锁

# maxSubThreadNumber = 10
#
#
# def task():
#     thName = threading.current_thread().name
#     print('start and wait run thread : %s' % thName)
#     eventLock.wait()
#     print('green light, carry on run thread : %s' % thName)
#     eventLock.wait()
#     print('green light222222, carry on run thread : %s' % thName)
#
#
# if __name__ == '__main__':
#     eventLock = threading.Event()
#     for i in range(maxSubThreadNumber):
#         subThreadIns = threading.Thread(target=task)
#         subThreadIns.start()
#
#     while True:
#         notifyNumber = int(
#             input('Please enter the numbers to running thread: '))
#         if notifyNumber == 1:
#             eventLock.set()  # 设置绿灯
#             eventLock.clear()  # 设置红灯
#         elif notifyNumber == 0:
#             eventLock.clear()  # 设置红灯
#         elif notifyNumber == 99:
#             break

# 信号量锁
maxSubThreadNumber = 6


def task():
    thName = threading.current_thread().name
    with semaLock:
        print('run sub thread {}'.format(thName))
        time.sleep(3)


if __name__ == '__main__':
    semaLock = threading.Semaphore(2)
    for i in range(maxSubThreadNumber):
        subThreadIns = threading.Thread(target=task)
        subThreadIns.start()
