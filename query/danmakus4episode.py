#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import logging
from dao import fetch_log_dao, danmaku_dao


def get_danmakus_by_episode(episode_id):
    return danmaku_dao.find_danmakus_by_episode(episode_id)


def get_dynamic_danmakus_by_episode(episode_id):
    fetch_logs = fetch_log_dao.find_fetch_logs_by_episode(episode_id)
    danmakus = danmaku_dao.find_danmakus_by_episode(episode_id)
    danmaku_lookup = dict()
    for danmaku in danmakus:
        danmaku_lookup[danmaku.raw_id] = danmaku
    splited_fetch_logs = dict()
    current_batch = None
    current_danmakus = []
    for fetch_log in fetch_logs:
        if fetch_log.batch != current_batch:
            splited_fetch_logs[current_batch] = current_danmakus
            current_batch = fetch_log.batch
            current_danmakus = []
            current_danmakus.append(fetch_log.danmaku)
        else:
            current_danmakus.append(fetch_log.danmaku)
    splited_fetch_logs[current_batch] = current_danmakus
    return splited_fetch_logs


if __name__ == "__main__":
    pass
