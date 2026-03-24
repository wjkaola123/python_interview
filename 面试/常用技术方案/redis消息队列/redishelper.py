import redis
import logging

logger = logging.getLogger(__name__)


class RedisHelper:
    """
    redis 帮助类
    """

    def __init__(self, host, port, db, channel, password=None):
        self.host = host
        self.port = port
        self.db = db
        self.channel = channel
        self.password = password
        self.__conn = redis.Redis(self.host, self.port, self.db, self.password, decode_responses=True)

    def ping(self):
        try:
            self.__conn.ping()
            return True
        except Exception as e:
            logger.exception(f"连接Redis失败，原因:{e}")
            return False

    # 发送消息
    def publish(self, msg):
        if self.ping():
            self.__conn.publish(self.channel, msg)
            return True
        else:
            return False

    # 订阅消息
    def subscribe(self):
        if self.ping():
            sub = self.__conn.pubsub()
            sub.subscribe(self.channel)
            sub.parse_response()
            return sub
