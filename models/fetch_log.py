#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, DateTime, BigInteger, ForeignKey
from sqlalchemy.orm import relationship, backref

from models.episode import Episode
from models.danmaku import Danmaku
from models import BaseModel

__BASE_MODEL = BaseModel.get_base_model()


class FetchLog(__BASE_MODEL):
    __tablename__ = 'fetch_log'
    id = Column(Integer, primary_key=True)
    batch = Column(Integer, nullable=True)
    createdAt = Column(DateTime, nullable=True)
    updatedAt = Column(DateTime, nullable=True)
    # 外键
    episode_id = Column(Integer, ForeignKey("episode.episode_id"))
    episode = relationship("Episode", backref=backref("fetch_logs", uselist=True, cascade="delete, all"))
    danmaku_id = Column(BigInteger, ForeignKey("danmaku.raw_id"))
    danmaku = relationship("Danmaku", backref=backref("fetch_logs", uselist=True, cascade="delete, all"))

    def __init__(self, data_dict):
        for key in data_dict:
            if hasattr(FetchLog, key):
                setattr(self, key, data_dict[key])
