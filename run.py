#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from tasks import index_page
from util.dbutil import DBUtil
from apscheduler.schedulers.blocking import BlockingScheduler


if __name__ == "__main__":
    db_util = DBUtil()
    db_util.init_db()
    index_page.index_page_spider()
    scheduler = BlockingScheduler()
    scheduler.add_job(index_page.index_page_spider, 'interval', minutes=120)
    scheduler.start()
