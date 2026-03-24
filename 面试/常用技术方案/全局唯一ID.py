import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from threading import Condition

import redis

BEGIN_TIMESTAMP = 1640995200
COUNT_BITS = 32


class RedisIdWorker:

    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    def next_id(self, key_prefix: str) -> int:
        # 1. 生成时间戳
        now_second = int(time.time())
        timestamp = now_second - BEGIN_TIMESTAMP
        # 2. 生成序列号
        key = f'icr:{key_prefix}:{datetime.now().strftime("%Y:%m:%d")}'
        count = self.redis_client.incr(key)
        # 3. 拼接Id
        return timestamp << COUNT_BITS | count


def task(id_worker: RedisIdWorker):
    for i in range(100):
        id = id_worker.next_id("order")
        print(f"id={id}")
    latch.countDown()


class CountDownLatch:

    def __init__(self, count):
        self.count = count
        self.condition = Condition()

    def wait(self):
        try:
            self.condition.acquire()
            while self.count > 0:
                self.condition.wait()
        finally:
            self.condition.release()

    def countDown(self):
        try:
            self.condition.acquire()
            self.count -= 1
            self.condition.notifyAll()
        finally:
            self.condition.release()

    def getCount(self):
        return self.count


if __name__ == '__main__':

    id_worker = RedisIdWorker()
    latch = CountDownLatch(300)
    begin = datetime.now()
    with ThreadPoolExecutor(max_workers=500) as executor:
        for i in range(600):
            executor.submit(task, id_worker)
    latch.wait()
    end = datetime.now()
    print(f"执行时间(s):{(end - begin).seconds}")
