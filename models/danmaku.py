#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Float, Text, Integer, DateTime, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, backref

from models import BaseModel

__BASE_MODEL = BaseModel.get_base_model()


class Danmaku(__BASE_MODEL):
    __tablename__ = 'danmaku'
    raw_id = Column(BigInteger, primary_key=True)  # 弹幕在弹幕数据库中rowID 用于“历史弹幕”功能
    playback_time = Column(Float, nullable=False)  # 弹幕出现的时间 以秒数为单位
    type = Column(Integer, nullable=False)  # 弹幕的模式1..3 滚动弹幕 4底端弹幕 5顶端弹幕 6.逆向弹幕 7精准定位 8高级弹幕
    font_size = Column(Integer, nullable=False)  # 字号， 12非常小,16特小,18小,25中,36大,45很大,64特别大
    font_color = Column(String(32), nullable=False)  # 字体的颜色 以HTML颜色的十位数为准
    unix_timestamp = Column(String(32), nullable=False)  # Unix格式的时间戳。基准时间为 1970-1-1 08:00:00
    pool = Column(Integer, nullable=False)  # 弹幕池 0普通池 1字幕池 2特殊池 【目前特殊池为高级弹幕专用】
    sender_id = Column(String(16), nullable=False)  # 发送者的ID，用于“屏蔽此弹幕的发送者”功能
    content = Column(Text, nullable=False)  # 弹幕内容
    createdAt = Column(DateTime, nullable=True)
    updatedAt = Column(DateTime, nullable=True)
    # 外键
    episode_aid = Column(Integer, ForeignKey("episode.av_id"))
    episode = relationship("Episode", backref=backref("danmakus", uselist=True, cascade="delete, all"))

    def __init__(self, attributes, content):
        attr_list = attributes.split(",")
        self.playback_time = attr_list[0]
        self.type = attr_list[1]
        self.font_size = attr_list[2]
        self.font_color = attr_list[3]
        self.unix_timestamp = attr_list[4]
        self.pool = attr_list[5]
        self.sender_id = attr_list[6]
        self.raw_id = int(attr_list[7])
        self.content = content
