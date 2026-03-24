import json

from 面试.常用技术方案.redis消息队列.redishelper import RedisHelper

obj = RedisHelper(host='127.0.0.1', port=6379, db=0, channel='channel:1')

for i in range(10):
    data = {
        "title": "aaaaaa",
        "description": "xxxxxxx",
        "id": i
    }
    obj.publish(json.dumps(data))
