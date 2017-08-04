#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import urllib2
import json
from tenacity import retry, stop_after_attempt, wait_fixed
import logging

logger = logging.getLogger("logger")


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def request_api(url):
    logger.info("Requesting url: " + url)
    response = urllib2.urlopen(url)
    return response.read()
