import gevent.monkey

gevent.monkey.patch_all()  # 修改内置的一些库为非阻塞

import gevent
import requests


def fetch(i):
    url = 'http://httpbin.org/get'
    resp = requests.get(url)
    print(len(resp.text), i)


def asynchronous():
    threads = []
    for i in range(10):
        threads.append(gevent.spawn(fetch, i))

    gevent.joinall(threads)


if __name__ == '__main__':
    print("Asynchronous:")
    asynchronous()
