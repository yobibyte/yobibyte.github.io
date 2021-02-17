#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'yobibyte'
SITENAME = "yobibyte's webpage"
SITETITLE = 'yobiblog'
SITESUBTITLE = 'Posts on Machine Learning, Reinforcement Learning, Learning from Demonstrations etc.'
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
THEME = "../Flex"
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
#PLUGINS = ['ipynb.markup', 'pelican-toc']
IGNORE_FILES = ['.ipynb_checkpoints']
SITELOGO = SITEURL + '/pics/socrat.png'

SOCIAL = (
          ('github', 'https://github.com/yobibyte'),
          ('twitter', 'https://twitter.com/y0b1byte'),
         )

MAIN_MENU = False
DISQUS_SITENAME = 'yobiblog-1'

GOOGLE_ANALYTICS= "UA-108066970-1"

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

#TOC = {
#    'TOC_HEADERS'       : '^h[1-6]', # What headers should be included in
#                                     # the generated toc
#                                     # Expected format is a regular expression
#
#    'TOC_RUN'           : 'true',    # Default value for toc generation,
#                                     # if it does not evaluate
#                                     # to 'true' no toc will be generated
#
#    'TOC_INCLUDE_TITLE': 'true',     # If 'true' include title in toc
#}
