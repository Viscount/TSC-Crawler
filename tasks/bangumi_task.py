#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import logging
import datetime
import time
import json
from request import webpage, api
from models.bangumi import Bangumi
from tasks import episode_task
from bs4 import BeautifulSoup
from dao import bangumi_dao


logger = logging.getLogger("logger")


def _construct_bangumi_detail_url(season_id):
    URL_HEADER = "http://bangumi.bilibili.com/jsonp/seasoninfo/"
    URL_FOOTER = ".ver?callback=seasonListCallback&jsonp=jsonp"
    return URL_HEADER + str(season_id) + URL_FOOTER


def _format_callback(callback_result):
    return callback_result[19:-2]


def get_style_tags(url):
    html_content = webpage.request_webpage(url)
    if html_content is None:
        return []
    web_page_content = BeautifulSoup(html_content, "html.parser")
    tag_list = web_page_content.find_all(class_="info-style-item")
    return [unicode(tag.string) for tag in tag_list]


def get_bangumi_actors(actor_list):
    actors = []
    for actor in actor_list:
        actors.append(actor['actor'])
    return actors


def bangumi_handler(data_dict):
    bangumi = Bangumi(data_dict)
    logger.info("Now collecting bangumi info :" + bangumi.season_id + "-" + bangumi.title + "...")
    bangumi.tags = "|".join(get_style_tags(bangumi.url))

    bangumi.createdAt = datetime.datetime.now()
    bangumi.updatedAt = datetime.datetime.now()

    bangumi_info = json.loads(_format_callback(api.request_api(_construct_bangumi_detail_url(bangumi.season_id))))
    bangumi.actors = "|".join(get_bangumi_actors(bangumi_info["result"]["actor"]))

    bangumi_dao.add_bangumi(bangumi)
    episodes_list = bangumi_info["result"]["episodes"]
    for episode_item in episodes_list:
        episode_task.episode_handler(bangumi, episode_item)
        time.sleep(1)
    return


if __name__ == "__main__":
    pass
