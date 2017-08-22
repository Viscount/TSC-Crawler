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
    parsed_content = BeautifulSoup(content, "xml", from_encoding="utf-8")
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
    for danmaku in raw_danmaku_list:
        danmaku.episode_id = episode.episode_id
        danmaku.createdAt = datetime.datetime.now()
        danmaku.updatedAt = datetime.datetime.now()
        exist_danmaku = danmaku_dao.find_danmaku(danmaku)
        if exist_danmaku is None:
            danmaku_dao.add_danmaku(danmaku)
            fetch_log = FetchLog({
                'batch': current_batch.id,
                'danmaku_id': danmaku.raw_id,
                'episode_id': episode.episode_id,
                'createdAt': datetime.datetime.now(),
                'updatedAt': datetime.datetime.now()
            })
        else:
            fetch_log = FetchLog({
                'batch': current_batch.id,
                'danmaku_id': exist_danmaku.raw_id,
                'episode_id': episode.episode_id,
                'createdAt': datetime.datetime.now(),
                'updatedAt': datetime.datetime.now()
            })
        fetch_log_dao.add_fetch_log(fetch_log)
    return


if __name__ == "__main__":
    get_danmaku_list(6888197)

