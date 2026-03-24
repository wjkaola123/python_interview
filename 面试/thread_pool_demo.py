import threading
import time
from concurrent.futures import ThreadPoolExecutor


def action(max):
    my_sum = 0
    for i in range(max):
        # print(threading.current_thread().name + ' ' + str(i))
        my_sum += i

    return my_sum


def get_result(future):
    print(future.alist())


with ThreadPoolExecutor(max_workers=2) as pool:
    future1 = pool.submit(action, 10000000)
    future1.add_done_callback(get_result)
    # future2 = pool.submit(action, 100)
    # print(future2.done())
    # print(future1.result())
    # print(future2.result())
    print('-' * 100)
