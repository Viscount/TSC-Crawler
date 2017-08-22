#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from util.dbutil import DBUtil


def add_fetch_log(fetch_log):
    session = DBUtil.open_session()
    try:
        session.merge(fetch_log)
        session.commit()
        return True
    except Exception as e:
        print e
        session.rollback()
        return False
    finally:
        DBUtil.close_session(session)


def add_fetch_logs(fetch_log_list):
    session = DBUtil.open_session()
    try:
        for fetch_log in fetch_log_list:
            session.merge(fetch_log)
        session.commit()
        return True
    except Exception as e:
        print e
        session.rollback()
        return False
    finally:
        DBUtil.close_session(session)
