# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import Column, String, create_engine, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 数据库连接信息
db_host = '******'
db_user = 'root'
db_pawd = 'roottoor'
db_name = 'music'
db_port = 3306

# 创建对象的基类:
Base = declarative_base()


class Music(Base):
    # 表名
    __tablename__ = 'music163'
    id = Column(Integer, unique=True, primary_key=True)
    song_id = Column(String(32))
    name = Column(String(1024))
    belong = Column(String(1024))
    down_url = Column(String(64))


class MusicPipeline(object):
    def __init__(self):
        # 初始化数据库连接,:
        engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'
                               .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def process_item(self, item, spider):
        print(item)
        info = Music(
            song_id=item["song_id"],
            name=item["name"],
            belong=item["belong"],
            down_url=item["down_url"],
        )
        self.session.add(info)
        self.session.commit()
        return item


if __name__ == "__main__":
    engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'
                           .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)
    Base.metadata.create_all(engine)
