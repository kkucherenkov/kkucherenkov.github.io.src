#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kirill Kucherenkov'
SITENAME = 'Yet Another Developer Journal [YADJ]'
SITEURL = 'kucherenkov.info'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = 'rss/all.xml'
CATEGORY_FEED_RSS = 'rss/%s.xml'
# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Linkedin','https://www.linkedin.com/in/kirillkucherenkov/'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISQUS_SITENAME = "kucherenkov-info"