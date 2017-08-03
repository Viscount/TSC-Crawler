#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from request import api

BASE_URL = "https://bangumi.bilibili.com/web_api/season/index_global?"
DEFAULT_PARAMETERS = {
                        "page": 1,
                        "page_size": 30,
                        "is_finish": 0,
                        "index_type": 1,
                        "index_sort": 0
                      }


def _construct_request_url():
    para_string = "&".join(key + "=" + str(DEFAULT_PARAMETERS[key]) for key in DEFAULT_PARAMETERS)
    return BASE_URL + para_string


def index_page_spider():
    data_dict = api.request_api(_construct_request_url())
    return data_dict

if __name__ == "__main__":
    print index_page_spider()
