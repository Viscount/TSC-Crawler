#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import logging
import datetime
from request import webpage
from models.danmaku import Danmaku
from models.fetch_log import FetchLog
from util.batch_singleton import BatchSingleton
from dao import danmaku_dao, fetch_log_dao
from bs4 import BeautifulSoup


logger = logging.getLogger("logger")


def get_danmaku_list(comment_id):
    HEADER_URL = "http://comment.bilibili.com/"
    content = webpage.request_webpage(HEADER_URL + str(comment_id) + ".xml")
    parsed_content = BeautifulSoup(content, "xml")
    raw_damakus = parsed_content.find_all("d")
    danmakus = []
    for raw_danmaku_line in raw_damakus:
        attr = raw_danmaku_line["p"]
        danmaku = Danmaku(attr, unicode(raw_danmaku_line.string))
        danmakus.append(danmaku)
    return danmakus


def danmaku_handler(episode):
    logger.info("Now collecting danmaku info :" + episode.cid + "...")
    raw_danmaku_list = get_danmaku_list(episode.cid)
    current_batch = BatchSingleton.get_instance()
    exist_danmakus = danmaku_dao.find_danmakus_by_episode(episode.episode_id)
    exist_raw_ids = set()
    for danmaku in exist_danmakus:
        exist_raw_ids.append(danmaku.raw_id)
    fetch_logs = []
    ready_danmakus = []
    for danmaku in raw_danmaku_list:
        danmaku.episode_id = episode.episode_id
        danmaku.createdAt = datetime.datetime.now()
        danmaku.updatedAt = datetime.datetime.now()
        fetch_log = FetchLog({
            'batch': current_batch.id,
            'danmaku_id': danmaku.raw_id,
            'episode_id': episode.episode_id,
            'createdAt': datetime.datetime.now(),
            'updatedAt': datetime.datetime.now()
        })
        if danmaku.raw_id not in exist_danmakus:
            ready_danmakus.append(danmaku)
        fetch_logs.append(fetch_log)
    danmaku_dao.add_danmakus(ready_danmakus)
    fetch_log_dao.add_fetch_logs(fetch_logs)
    return


if __name__ == "__main__":
    get_danmaku_list(6888197)

