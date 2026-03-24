import asyncio
import datetime
import random
import time


# async def simple_async():
#     print('hello')
#     await asyncio.sleep(1)
#     print('python')
#
#
# asyncio.run(simple_async())


# async def do_something(index):
#     print(f'start at {time.strftime("%X")}', index)
#     await asyncio.sleep(2)
#     print(f'finished at {time.strftime("%X")}', index)
#
#
# def test():
#     tasks = [do_something(i) for i in range(5)]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#     loop.close()


# test()


# async def do_after(what, deplay):
#     await asyncio.sleep(deplay)
#     print(what)
#
#
# async def corun():
#     print(f'enter corun at {time.strftime("%X")}')
#     task1 = asyncio.create_task(do_after('hello', 1))
#     task2 = asyncio.create_task(do_after('python', 2))
#     print(f'start at {time.strftime("%X")}')
#     await task1
#     await task2
#
#     print(f'finished at {time.strftime("%X")}')


# asyncio.run(corun())

# async def gather():
#     print(f'start at {time.strftime("%X")}')
#     await asyncio.gather(do_after('hello', 1), do_after('python', 2))
#     print(f'finished at {time.strftime("%X")}')


# asyncio.run(gather())


async def display_date(num, loop):
    end_time = loop.time() + 10.0
    while True:
        print('Num: {} Time: {}'.format(num, datetime.datetime.now()))
        if loop.time() + 1.0 >= end_time:
            print('looptime:{}, Num:{}'.format(loop.time(), num))
            break
        await asyncio.sleep(random.randint(0, 5))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(display_date(1, loop))
    asyncio.ensure_future(display_date(2, loop))
    asyncio.ensure_future(display_date(3, loop))
    loop.run_forever()
    # loop.run_until_complete(future)
