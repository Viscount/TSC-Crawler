#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import logging
import datetime
import json
from request import webpage, api
from models.bangumi import Bangumi
from tasks import episode
from bs4 import BeautifulSoup
from dao import bangumi_dao


logger = logging.getLogger("logger")


def _construct_bangumi_detail_url(season_id):
    URL_HEADER = "http://bangumi.bilibili.com/jsonp/seasoninfo/"
    URL_FOOTER = ".ver?callback=seasonListCallback&jsonp=jsonp"
    return URL_HEADER + str(season_id) + URL_FOOTER


def _format_callback(callback_result):
    return callback_result[19:-2]


def get_style_tags(web_page_content):
    tag_list = web_page_content.find_all(class_="info-style-item")
    return [unicode(tag.string) for tag in tag_list]


def bangumi_handler(data_dict):
    bangumi = Bangumi(data_dict)
    logger.info("Now collecting bangumi info :" + bangumi.season_id + "-" + bangumi.title + "...")
    web_page_content = BeautifulSoup(webpage.request_webpage(bangumi.url), "html.parser")
    bangumi.tags = "|".join(get_style_tags(web_page_content))
    bangumi.createdAt = datetime.datetime.now()
    bangumi.updatedAt = datetime.datetime.now()
    bangumi_dao.add_bangumi(bangumi)

    bangumi_info = json.loads(_format_callback(api.request_api(_construct_bangumi_detail_url(bangumi.season_id))))
    episodes_list = bangumi_info["result"]["episodes"]
    for episode_item in episodes_list:
        episode.episode_handler(episode_item)
    return


if __name__ == "__main__":
    pass
