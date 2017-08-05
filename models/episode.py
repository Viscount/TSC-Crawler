#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Text, Integer, DateTime

from models import BaseModel

__BASE_MODEL = BaseModel.get_base_model()


class Episode(__BASE_MODEL):
    __tablename__ = 'episode'
    id = Column(Integer, primary_key=True)
    av_id = Column(Integer, nullable=False)
    cid = Column(Integer, nullable=False)
    coins = Column(Integer, nullable=True)
    cover = Column(String, nullable=True)
    episode_id = Column(Integer, nullable=False)
    episode_status = Column(Integer, nullable=True)
    index = Column(String, nullable=True)
    index_title = Column(String, nullable=True)
    update_time = Column(DateTime, nullable=False)
    createdAt = Column(DateTime, nullable=True)
    updatedAt = Column(DateTime, nullable=True)

    def __init__(self, data_dict):
        for key in data_dict:
            if hasattr(Episode, key):
                setattr(self, key, data_dict[key])
