#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import time
from dao import batch_dao
from models.batch import Batch


class BatchSingleton():
    __instance__ = None

    @staticmethod
    def get_instance():
        if BatchSingleton.__instance__ is None:
            new_batch_dict = {
                "status": "PROCESSING",
                "createdAt": time.localtime(time.time()),
                "updatedAt": time.localtime(time.time())
            }
            BatchSingleton.__instance__ = batch_dao.add_batch(Batch(new_batch_dict))
            return BatchSingleton.__instance__
        else:
            return BatchSingleton.__instance__


    @staticmethod
    def clean_instance():
        if BatchSingleton.__instance__ is not None:
            BatchSingleton.__instance__.status = 'STOPED'
            batch_dao.update_batch(BatchSingleton.__instance__)
        BatchSingleton.__instance__ = None
        return
