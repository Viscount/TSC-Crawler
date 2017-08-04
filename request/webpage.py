#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import urllib2
import logging
from tenacity import retry, stop_after_attempt, wait_fixed

logger = logging.getLogger("logger")


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def request_webpage(url):
    logger.info("Requesting url: " + url)
    response = urllib2.urlopen(url)
    return response.read()
