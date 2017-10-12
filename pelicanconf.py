#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'yobibyte'
SITENAME = "yobibyte's webpage"
SITETITLE = 'yobiblog'
SITESUBTITLE = 'posts on Machine Learning, Reinforcement Learning, Learning from Demonstrations etc.'
SITEURL = 'http://yobibyte.github.io'
PATH = 'content'
TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = "/home/yobibyte/dev/Flex"
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IGNORE_FILES = ['.ipynb_checkpoints']
SITELOGO = SITEURL + '/pics/socrat.png'

SOCIAL = (
          ('github', 'https://github.com/yobibyte'),
          ('twitter', 'https://twitter.com/y0b1byte'),
         )

MAIN_MENU = False

GOOGLE_ANALYTICS = 'UA-108066970-1'

