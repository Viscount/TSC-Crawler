#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from util.dbutil import DBUtil
from dao import logger
from models.bangumi import Bangumi


def add_bangumi(bangumi):
    session = DBUtil.open_session()
    try:
        session.merge(bangumi)
        session.commit()
        return True
    except Exception as e:
        print e
        session.rollback()
        return False
    finally:
        DBUtil.close_session(session)


def add_bangumis(bangumi_list):
    session = DBUtil.open_session()
    try:
        for bangumi in bangumi_list:
            session.merge(bangumi)
        session.commit()
        return True
    except Exception as e:
        print e
        session.rollback()
        return False
    finally:
        DBUtil.close_session(session)
