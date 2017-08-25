#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from util.dbutil import DBUtil
from models.danmaku import Danmaku


def add_danmaku(danmaku):
    session = DBUtil.open_session()
    try:
        session.merge(danmaku)
        session.commit()
        return True
    except Exception as e:
        print e
        session.rollback()
        return False
    finally:
        DBUtil.close_session(session)


def add_danmakus(danmaku_list):
    session = DBUtil.open_session()
    try:
        for danmaku in danmaku_list:
            session.merge(danmaku)
        session.commit()
        return True
    except Exception as e:
        print e
        session.rollback()
        return False
    finally:
        DBUtil.close_session(session)


def find_danmaku(danmaku):
    session = DBUtil.open_session()
    try:
        result = session.query(Danmaku).filter(Danmaku.raw_id == danmaku.raw_id).first()
        return result
    except Exception as e:
        print e
        session.rollback()
        return None
    finally:
        DBUtil.close_session(session)


def find_danmakus_by_episode(episode_id):
    session = DBUtil.open_session()
    try:
        result = session.query(Danmaku).filter(Danmaku.episode_id == episode_id).all()
        return result
    except Exception as e:
        print e
        session.rollback()
        return None
    finally:
        DBUtil.close_session(session)
