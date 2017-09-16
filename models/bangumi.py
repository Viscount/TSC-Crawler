#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Text, Integer, DateTime

from models import BaseModel

__BASE_MODEL = BaseModel.get_base_model()


class Bangumi(__BASE_MODEL):
    __tablename__ = 'bangumi'
    cover = Column(Text, nullable=True)
    favorites = Column(Integer, nullable=True)
    is_finish = Column(Integer, nullable=True)
    newest_ep_index = Column(String(16), nullable=True)
    pub_time = Column(Integer, nullable=True)
    season_id = Column(Integer, primary_key=True)
    season_status = Column(Integer, nullable=True)
    title = Column(String(64), nullable=True)
    introduction = Column(String(512), nullable=True)
    total_count = Column(Integer, nullable=True)
    update_time = Column(Integer, nullable=True)
    url = Column(Text, nullable=True)
    week = Column(String(30), nullable=True)
    tags = Column(Text, nullable=True)
    actors = Column(Text, nullable=True)
    createdAt = Column(DateTime, nullable=True)
    updatedAt = Column(DateTime, nullable=True)

    def __init__(self, data_dict):
        for key in data_dict:
            if hasattr(Bangumi, key):
                setattr(self, key, data_dict[key])
