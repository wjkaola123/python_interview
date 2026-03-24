# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
from itemadapter import ItemAdapter
import sqlite3

logger = logging.getLogger(__name__)


class SqlitePipeline:
    def __init__(self):
        logger.info("SqlitePipeline 初始化：__init__() 被调用")
        self.conn = None
        self.cursor = None
    
    def open_spider(self, spider):
        """打开数据库连接和游标"""
        logger.info(f"open_spider() 被调用 - Spider 名称：{spider.name}")
        logger.info("正在连接数据库...")
        self.conn = sqlite3.connect('games.db')
        self.cursor = self.conn.cursor()
        
        # 创建表（如果不存在）
        logger.info("正在创建数据表...")
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                game_name TEXT NOT NULL,
                game_link TEXT,
                game_category TEXT,
                game_date TEXT
            )
        ''')
        self.conn.commit()
        
        # 清空表（可选，如果需要保留历史数据请注释掉）
        logger.info("正在清空旧数据...")
        self.cursor.execute('DELETE FROM games')
        self.conn.commit()
        logger.info("数据库准备就绪！")
    
    def close_spider(self, spider):
        """关闭数据库连接"""
        logger.info(f"close_spider() 被调用 - Spider 名称：{spider.name}")
        logger.info("正在关闭数据库连接...")
        self.conn.close()
        logger.info("数据库连接已关闭")
    
    def process_item(self, item, spider):
        """处理每个爬取到的数据项"""
        self.cursor.execute('''
            INSERT INTO games (game_name, game_link, game_category, game_date)
            VALUES (?, ?, ?, ?)
        ''', (
            item.get('game_name'),
            item.get('game_link'),
            item.get('game_category'),
            item.get('game_date')
        ))
        self.conn.commit()
        return item
