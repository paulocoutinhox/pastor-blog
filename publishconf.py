#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://pastorpaulo.com"

FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feed/rss.xml"
# CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
# TAG_FEED_RSS = "feeds/tags/{slug}.xml"

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = "pastor-paulo"
GOOGLE_ANALYTICS = "UA-148725195-1"
