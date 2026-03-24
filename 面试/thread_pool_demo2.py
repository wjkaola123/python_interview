import threading
import time
from concurrent.futures import ThreadPoolExecutor


def action(max):
    my_sum = 0
    for i in range(max):
        # print(threading.current_thread().name + ' ' + str(i))
        my_sum += i

    return my_sum


with ThreadPoolExecutor(max_workers=4) as pool:
    results = pool.map(action, (50, 100, 150))
    print('-' * 10)
    for r in results:
        print(r)
