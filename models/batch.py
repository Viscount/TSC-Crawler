#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime
from models import BaseModel

__BASE_MODEL = BaseModel.get_base_model()


class Batch(__BASE_MODEL):
    __tablename__ = 'batch'
    id = Column(Integer, primary_key=True)
    status = Column(String(30), nullable=False)
    createdAt = Column(DateTime, nullable=True)
    updatedAt = Column(DateTime, nullable=True)

    def __init__(self, data_dict):
        for key in data_dict:
            if hasattr(Batch, key):
                setattr(self, key, data_dict[key])

