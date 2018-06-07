#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marek Nožka'
SITENAME = u'Marrek.cz'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = u'cs'
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'Blog'

THEME = 'theme-simplegray/'

TYPOGRIFY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GITHUB_URL = 'https://github.com/marreknozka/marreknozka.github.io'

# Blogroll
LINKS = (
    ('www.jezisuzdravuje.cz', 'http://www.jezisuzdravuje.cz'),
    ('www.vojtechkodet.cz', 'http://www.vojtechkodet.cz'),
    ('Milujte se', 'http://milujte.se'),
    ('Ron Wyatt', 'http://www.b-a-n.cz/informace.html'),
    ('Stvoření?', 'http://www.stvoreni.cz/'),
    ('Manželství.cz', 'http://www.manzelstvi.cz/'),
    ('Maria.cz', 'http://www.maria.cz/'),
    ('Jsem pro život', 'http://prolife.cz/'),
    ('Kurzy α', 'http://www.kurzyalfa.cz/'),
    ('MatPlotLib', 'http://matplotlib.org'),
    ('NumPy', 'http://www.numpy.org/'),
    ('SciPy', 'http://scipy.org/'),
    ('Zim - A Desktop Wiki', 'http://zim-wiki.org/'),
    ('VOŠ a SPŠe Olomouc', 'http://www.spseol.cz/'),
    ('Antispam', 'http://antispam.er.cz/'),
    # ('Check I/O', 'http://www.checkio.org/'),
    ('Oprava trekové obuvy', 'http://www.trekovaobuv.eu/'),
    ('searchcode.com', 'https://searchcode.com/'),
    # ('', ''),
)
# Social widget
SOCIAL = (
    ('Github', 'http://github.com/MarrekNozka'),
    ('Twitter', 'http://twitter.com/MarrekNozka'),
    ('YouTube', 'https://www.youtube.com/user/YouTlapickaTube'),
    ('Flickr', 'http://www.flickr.com/photos/tlapicka/'),
    ('Wikipedista', 'http://cs.wikipedia.org/wiki/Wikipedista:Tlapicka'),
    ('Wikiobčan',
        'http://commons.wikimedia.org/wiki/Special:ListFiles/Tlapicka'),
    ('Wikispisovatel', 'http://cs.wikibooks.org/wiki/User:Tlapicka'),
    ('Mamut', 'http://mamut.spseol.cz/nozka/'),
)

DEFAULT_PAGINATION = 20

# MARKDOWN = [
#     'codehilite(css_class=highlight)',
#     'extra',
#     'headerid(level=2)',
#     'toc',
#     'linksShortcuts:Shortcuts',
# ]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.headerid': {'level': 2},
    },
    'output_format': 'html5',
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['img', 'images', 'extra/CNAME', 'src', 'data']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
