import time


def count_time_wrapper(func):
    def improved_func():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"it takes {end_time - start_time}s to find all the olds")

    return improved_func


@count_time_wrapper
def find_olds():
    olds = []
    for i in range(100000000):
        if i % 2 == 0:
            olds.append(i)
    return olds

find_olds()