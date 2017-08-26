#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from util.dbutil import DBUtil
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


def find_bangumi_by_id(season_id):
    session = DBUtil.open_session()
    try:
        result = session.query(Bangumi).filter(Bangumi.season_id == season_id).first()
        return result
    except Exception as e:
        print e
        session.rollback()
        return None
    finally:
        DBUtil.close_session(session)
