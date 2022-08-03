# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://pastorpaulo.com"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feed/rss.xml"
# CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
# TAG_FEED_RSS = "feeds/tags/{slug}.xml"

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = "pastor-paulo"
GOOGLE_ANALYTICS = "G-19HME37XFP"
MICROSOFT_CLARITY = "d1r7jqisp3"
