#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import urllib2
import json
from tenacity import retry, stop_after_attempt, wait_fixed


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def request_api(url):
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    return data
