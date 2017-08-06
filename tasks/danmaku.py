#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import logging
import datetime
from request import webpage
from models.danmaku import Danmaku
from dao import danmaku_dao
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
    for danmaku in raw_danmaku_list:
        danmaku.episode = episode
        danmaku.createdAt = datetime.datetime.now()
        danmaku.updatedAt = datetime.datetime.now()

    danmaku_dao.add_danmakus(raw_danmaku_list)
    return


if __name__ == "__main__":
    get_danmaku_list(6888197)

