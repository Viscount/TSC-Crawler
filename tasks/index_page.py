#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import logging
import time
import json
from request import api
from tasks import bangumi_task
from util.batch_singleton import BatchSingleton


BASE_URL = "https://bangumi.bilibili.com/web_api/season/index_global?"
DEFAULT_PARAMETERS = {
                        "page": 1,
                        "page_size": 30,
                        "is_finish": 0,
                        "index_type": 1,
                        "index_sort": 0
                      }
logger = logging.getLogger("logger")
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)


# 构造获取番剧列表信息的请求url
def _construct_request_url(**kwargs):
    if kwargs is not None:
        for key in kwargs:
            if key in DEFAULT_PARAMETERS:
                DEFAULT_PARAMETERS[key] = kwargs[key]
    para_string = "&".join(key + "=" + str(DEFAULT_PARAMETERS[key]) for key in DEFAULT_PARAMETERS)
    return BASE_URL + para_string


# 番剧列表页面爬虫
def index_page_spider(page_query_interval=1):
    page_number = 1
    while True:
        logger.info("Collecting in index page " + str(page_number) + "...")
        data_dict = json.loads(api.request_api(_construct_request_url(page=page_number)))
        result = data_dict["result"]
        bangumi_list = result["list"]
        for bangumi_info in bangumi_list:
            bangumi_task.bangumi_handler(bangumi_info)
        if page_number >= 30:
            break
        else:
            page_number += 1
            time.sleep(page_query_interval)
    BatchSingleton.clean_instance()
    return

if __name__ == "__main__":
    index_page_spider()
