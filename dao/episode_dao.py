#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from util.dbutil import DBUtil
from models.episode import Episode


def add_episode(episode):
    session = DBUtil.open_session()
    try:
        session.merge(episode)
        session.commit()
        return True
    except Exception as e:
        print e
        session.rollback()
        return False
    finally:
        DBUtil.close_session(session)


def add_episodes(episode_list):
    session = DBUtil.open_session()
    try:
        for episode in episode_list:
            session.merge(episode)
        session.commit()
        return True
    except Exception as e:
        print e
        session.rollback()
        return False
    finally:
        DBUtil.close_session(session)
