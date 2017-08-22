#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from util.dbutil import DBUtil
from models.batch import Batch


def add_batch(batch):
    session = DBUtil.open_session()
    try:
        session.add(batch)
        session.commit()
        session.refresh(batch)
        return batch
    except Exception as e:
        print e
        session.rollback()
        return None
    finally:
        DBUtil.close_session(session)


def update_batch(batch):
    session = DBUtil.open_session()
    try:
        session.merge(batch)
        session.commit()
        return True
    except Exception as e:
        print e
        session.rollback()
        return False
    finally:
        DBUtil.close_session(session)

