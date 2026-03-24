import gevent.monkey

gevent.monkey.patch_all()

import gevent
import requests


def fetch(i):
    url = 'http://httpbin.org/get'
    resp = requests.get(url, params={'a': 1, 'b': 2})
    print(resp.text, i)


def asyncchronous():
    threads = []
    for i in range(1, 5):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


print('Asyncchronous:')
asyncchronous()
