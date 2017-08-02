# -*- coding: utf-8 -*-
import scrapy


def construct_query_url(basic_url_header, index_type, index_sort, page):
    return basic_url_header + "index_type=" + str(index_type) + "&index_sort=" + str(index_sort) \
           + "&page=" + str(page)


class BangumiSpider(scrapy.Spider):
    name = 'bangumi'
    allowed_domains = ['bangumi.bilibili.com']
    basic_url_header = 'http://bangumi.bilibili.com/web_api/season/index_global?'
    index_type = 1  # 按追番人数排列
    index_sort = 0  # 按从大到小排列
    page = 1

    start_urls = [construct_query_url(basic_url_header, index_type, index_sort, page)]

    def parse(self, response):
        print response.body
