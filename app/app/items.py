# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Danmaku(scrapy.Item):
    row_id = scrapy.Field()
    play_timestamp = scrapy.Field()
    type = scrapy.Field()
    font_size = scrapy.Field()
    font_color = scrapy.Field()
    unix_timestamp = scrapy.Field()
    pool = scrapy.Field()
    sender_id = scrapy.Field()
    content = scrapy.Field()


class Bangumi(scrapy.Item):
    cover = scrapy.Field()
    favorites = scrapy.Field()
    season_id = scrapy.Field()
    season_status = scrapy.Field()
    title = scrapy.Field()
    is_finish = scrapy.Field()
    pub_time = scrapy.Field()
    url = scrapy.Field()
    tags = scrapy.Field()
