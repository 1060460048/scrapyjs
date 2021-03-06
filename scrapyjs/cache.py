# -*- coding: utf-8 -*-
"""
To handle "splash" Request meta key correctly when HTTP cache is enabled
Scrapy needs a custom caching backed.

See https://github.com/scrapy/scrapy/issues/900 for more info.
"""
from __future__ import absolute_import
import os

from scrapy.contrib.httpcache import FilesystemCacheStorage

from .dupefilter import splash_request_fingerprint


class SplashAwareFSCacheStorage(FilesystemCacheStorage):
    def _get_request_path(self, spider, request):
        key = splash_request_fingerprint(request)
        return os.path.join(self.cachedir, spider.name, key[0:2], key)
