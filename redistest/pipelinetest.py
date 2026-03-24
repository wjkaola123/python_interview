# -*- coding:utf-8 -*-
from threading import Thread

import redis
import time
from concurrent.futures import ProcessPoolExecutor, as_completed, ThreadPoolExecutor

r = redis.Redis(host='127.0.0.1', port=6379, db=0)


def try_pipeline():
    start = time.time()
    with r.pipeline(transaction=False) as p:
        p.sadd('seta', 1).sadd('seta', 2).sadd('seta', 3).lpush('lista', 1).lpush('lista', 0)
        p.execute()
    print(time.time() - start)


def without_pipeline():
    start = time.time()
    r.sadd('seta', 1)
    r.sadd('seta', 2)
    r.srem('seta', 2)
    r.lpush('lista', 1)
    r.lrange('lista', 0, -1)
    print(time.time() - start)


def worker():
    while True:
        try_pipeline()


with ThreadPoolExecutor(max_workers=1) as pool:
    pool.submit(worker)
