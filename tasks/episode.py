#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import logging
import json
import datetime
from request import webpage, api
from models.episode import Episode
from tasks import danmaku

logger = logging.getLogger("logger")


def _construct_cid_query_url(episode_id):
    URL_HEADER = "https://bangumi.bilibili.com/web_api/episode/"
    URL_FOOTER = ".json"
    return URL_HEADER + str(episode_id) + URL_FOOTER


def get_comment_id(episode_id):
    result = json.loads(api.request_api(_construct_cid_query_url(episode_id)))
    return result["result"]["currentEpisode"]["danmaku"]


def episode_handler(data_dict):
    episode = Episode(data_dict)
    episode.cid = get_comment_id(episode.episode_id)
    episode.createdAt = datetime.datetime.now()
    episode.updatedAt = datetime.datetime.now()

    danmaku.danmaku_handler(episode.cid)
    return
