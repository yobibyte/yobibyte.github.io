#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelican_jupyter import markup as nb_markup

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
PLUGINS = [nb_markup]
IGNORE_FILES = ['.ipynb_checkpoints']
SITELOGO = SITEURL + '/pics/socrat.png'

SOCIAL = (
          ('github', 'https://github.com/yobibyte'),
          ('twitter', 'https://twitter.com/y0b1byte'),
         )

MAIN_MENU = True
LINKS = (
    ("talks", "https://www.notion.so/talks-d996faf8121241cebc89ea0c782c6322"),
    ("paper notes", "https://www.notion.so/Paper-Notes-by-Vitaly-Kurin-97827e14e5cd4183815cfe3a5ecf2f4c"),
)

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
