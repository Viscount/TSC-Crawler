#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import logging
from dao import bangumi_dao, danmaku_dao


def get_danmakus_by_bangumi(bangumi_season_id):
    bangumi = bangumi_dao.find_bangumi_by_id(bangumi_season_id)
    danmakus4bangumi = dict()
    for episode in bangumi.episodes:
        danmaku_list = danmaku_dao.find_danmakus_by_episode(episode.episode_id)
        danmakus4bangumi[episode.episode_id] = danmaku_list
    return danmakus4bangumi

if __name__ == "__main__":
    print len(get_danmakus_by_bangumi(3461))

