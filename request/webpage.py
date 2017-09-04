#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import urllib2
import logging
import zlib
from tenacity import retry, stop_after_attempt, wait_fixed

logger = logging.getLogger("logger")

HEADER = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)' +
                          ' Chrome/48.0.2564.116 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def request_webpage(url):
    try:
        logger.info("Requesting url: " + url)
        req = urllib2.Request(url, headers=HEADER)
        response = urllib2.urlopen(req, timeout=2)
        content = response.read()
        logger.info("Response: " + str(response.code))
        response.close()
        resp_info = response.info()

        if resp_info["Content-Encoding"] == "deflate":
            content = zlib.decompress(content, -zlib.MAX_WBITS)
        elif resp_info["Content-Encoding"] == "gzip":
            content = zlib.decompress(content, zlib.MAX_WBITS | 16)
        elif resp_info["Content-Encoding"] == "zlib":
            content = zlib.decompress(content, zlib.MAX_WBITS)

        return content
    except zlib.error as exception:
        print exception
        logger.debug(exception)
        return None
    except Exception as e:
        print e
        return None

