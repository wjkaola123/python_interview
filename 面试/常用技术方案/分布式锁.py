import threading
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed

import redis
import time


class RedisLock:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
        self._lock_id = None

    def get_lock(self, name, timeout):
        """
        :param name: 锁名
        :param timeout: 超时时间
        :return: 成功返回锁值，失败返回False
        """
        val = self.redis_client.get(name)
        if val:
            return False
        self._lock_id = str(uuid.uuid4())
        lock_val = f'{self._lock_id}'
        return self.redis_client.set(name, lock_val, ex=timeout, nx=True)

    def release_lock(self, name):
        """
        :param name: 锁名
        :return: 成功返回锁值，失败返回False
        """
        pipe = self.redis_client.pipeline(True)
        while True:
            try:
                # 通过watch命令监视某个键，该键未被其它客户端修改值时，事务执行成功。
                pipe.watch(name)
                print(str(pipe.get(name), 'utf-8'))
                print(f'{self._lock_id}')
                if str(pipe.get(name), 'utf-8') == f'{self._lock_id}':
                    # multi 命令开启一个事务
                    pipe.multi()
                    pipe.delete(name)
                    pipe.execute()
                    return True
                pipe.unwatch()
                break
            except redis.exceptions.WatchError as e:
                print(str(e))
        return False

        # val = self.redis_client.get(name)
        # if not val:
        #     return True
        # if str(val, 'utf-8') == f'locked_{self._lock_id}':
        #     self.redis_client.delete(name)
        #     return True
        # return False


if __name__ == '__main__':
    cli = RedisLock()
    lock_name = 'mylock1'
    cli2 = RedisLock()
    # re1 = cli.get_lock('mylock1', 10)
    # print(re1)
    # re2 = cli.get_lock('mylock1', 20)
    # print(re2)
    # rr = cli2.release_lock('mylock1')  # 用其他对象解锁，会失败
    # print(rr)
    # re3 = cli.release_lock('mylock1')
    # print(re3)
    # # time.sleep(1)
    # re4 = cli.get_lock('mylock1', 20)
    # print(re4)

    # 多线程竞争抢锁,只有一个线程获取成功
    pool = ThreadPoolExecutor(max_workers=50)
    all_task = [pool.submit(cli.get_lock, *[lock_name, i]) for i in range(1, 100)]
    for future in as_completed(all_task):
        data = future.result()
        print('result:', data)

# task0 = pool.submit(cli.get_lock, lock_name, 10)
# task1 = pool.submit(cli.get_lock, lock_name, 10)
# task2 = pool.submit(cli.get_lock, lock_name, 30)
# res0 = task0.result()
# res1 = task1.result()
# res2 = task2.result()
# print('res0:', res0)
# print('res1:', res1)
# print('res2:', res2)

# task3 = pool.submit(cli2.release_lock, lock_name)  # 其它对象解锁
# res3 = task3.result()
# task4 = pool.submit(cli.release_lock, lock_name)
# res4 = task4.result()
# print(f'res3:{res3}')
# print(f'res4:{res4}')
