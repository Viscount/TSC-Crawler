#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Text
from sqlalchemy.orm import relationship, backref

from models import BaseModel

__BASE_MODEL = BaseModel.get_base_model()


class Episode(__BASE_MODEL):
    __tablename__ = 'episode'
    av_id = Column(Integer, nullable=False)
    cid = Column(Integer, nullable=False)
    coins = Column(Integer, nullable=True)
    cover = Column(Text, nullable=True)
    episode_id = Column(Integer, primary_key=True)
    episode_status = Column(Integer, nullable=True)
    index = Column(String(32), nullable=True)
    index_title = Column(String(64), nullable=True)
    tags = Column(Text, nullable=True)
    update_time = Column(DateTime, nullable=False)
    createdAt = Column(DateTime, nullable=True)
    updatedAt = Column(DateTime, nullable=True)
    # 外键
    season_id = Column(Integer, ForeignKey("bangumi.season_id"))
    bangumi = relationship("Bangumi", backref=backref("episodes", uselist=True, cascade="delete, all"))

    def __init__(self, data_dict):
        for key in data_dict:
            if hasattr(Episode, key):
                setattr(self, key, data_dict[key])
