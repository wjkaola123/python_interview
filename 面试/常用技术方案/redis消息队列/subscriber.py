import json
import logging

from 面试.常用技术方案.redis消息队列.redishelper import RedisHelper

logger = logging.getLogger(__name__)
obj = RedisHelper(host='127.0.0.1', port=6379, db=0, channel='channel:1')

sub_obj = obj.subscribe()
while True:
    if sub_obj:
        msg = sub_obj.parse_response()
        info_dict = json.loads(msg[2])
        print(info_dict)
    else:
        break
