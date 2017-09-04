#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import urllib2
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception_type
from urllib2 import URLError
from socket import timeout
from ssl import SSLError
import logging

logger = logging.getLogger("logger")


@retry(retry=retry_if_exception_type(URLError) | retry_if_exception_type(timeout) | retry_if_exception_type(SSLError),
       stop=stop_after_attempt(3), wait=wait_fixed(1))
def request_api(url):
    try:
        logger.info("Requesting url: " + url)
        response = urllib2.urlopen(url, timeout=10)
        logger.info("Response: " + str(response.code))
        return response.read()
    except Exception as e:
        print type(e), e

