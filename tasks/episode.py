#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import logging
import json
import datetime
from request import webpage, api
from models.episode import Episode
from tasks import danmaku
from dao import episode_dao
from bs4 import BeautifulSoup

logger = logging.getLogger("logger")


def _construct_cid_query_url(episode_id):
    URL_HEADER = "https://bangumi.bilibili.com/web_api/episode/"
    URL_FOOTER = ".json"
    return URL_HEADER + str(episode_id) + URL_FOOTER


def get_comment_id(episode_id):
    result = json.loads(api.request_api(_construct_cid_query_url(episode_id)))
    return result["result"]["currentEpisode"]["danmaku"]


def get_tag_list(av_id):
    URL_HEADER = "http://api.bilibili.com/x/tag/archive/tags?aid="
    result = json.loads(api.request_api(URL_HEADER + str(av_id)))
    tag_list = result["data"]
    return [tag["tag_name"] for tag in tag_list]


def episode_handler(bangumi, data_dict):
    episode = Episode(data_dict)
    logger.info("Now collecting episode info :" + episode.episode_id + "-" + episode.index_title + "...")
    episode.cid = get_comment_id(episode.episode_id)
    episode.tags = "|".join(get_tag_list(episode.av_id))
    episode.season_id = bangumi.season_id
    episode.createdAt = datetime.datetime.now()
    episode.updatedAt = datetime.datetime.now()
    episode_dao.add_episode(episode)

    danmaku.danmaku_handler(episode)
    return
