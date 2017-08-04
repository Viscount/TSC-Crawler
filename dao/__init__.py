#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from util.dbutil import DBUtil
import logging

DBUtil.init_db()
logger = logging.getLogger("logger")
