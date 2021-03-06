#!/usr/bin/env python3.8
# -*- coding: utf-8 -*- #


AUTHOR = "MarrekNozka"
SITENAME = "Marrek.cz"
SITEURL = ""

PATH = "content"

THEME = "../elegant/"
RECENT_ARTICLES_COUNT = 42
USE_SHORTCUT_ICONS = True
SOCIAL_PROFILE_LABEL = "Kontakt"
LANDING_PAGE_TITLE = "Marrkův blog"
PROJECTS_TITLE = "Moje projekty"
TYPOGRIFY = True

RECENT_ARTICLE_SUMMARY = True

TAG_CLOUD_STEPS = 6
TAG_CLOUD_MAX_ITEMS = 200

TIMEZONE = "Europe/Prague"
DEFAULT_LANG = "cs"
DEFAULT_DATE = "fs"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ["extract_toc"]

PLUGINS += ["tipue_search"]
DIRECT_TEMPLATES = ["index", "categories", "tags", "archives"]
DIRECT_TEMPLATES += ["search"]

PLUGINS.append("jinja2content")
JINJA2CONTENT_TEMPLATES = ["."]

PLUGINS += ["liquid_tags", "liquid_tags.include_code"]
CODE_DIR = "code"

PLUGINS += ["related_posts"]
RELATED_POSTS_MAX = 12
RELATED_POSTS_LABEL = "Související posty"

PLUGINS += ["series"]
SERIES_TITLE = "Další posty v této sérii"

PLUGINS += ["render_math"]

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget
SOCIAL = (
    ("email", "marrek&#32;z&#64;vináč&#32;marrek&#32;tečka&#32;cz"),
    ("GitLab", "https://gitlab.com/MarrekNozka"),
    ("GitHub", "https://github.com/MarrekNozka"),
    ("Twitter", "https://twitter.com/MarrekNozka"),
    ("YouTube", "https://www.youtube.com/c/MarekNožka"),
    ("reddit", "https://www.reddit.com/user/MarrekNozka"),
    ("StackOverflow", "https://stackoverflow.com/users/2188314/marreknožka"),
    ("Telegram", "https://t.me/MarrekNozka"),
    ("flicker", "https://www.flickr.com/photos/tlapicka/"),
    ("Wikipedia", "http://cs.wikipedia.org/wiki/Wikipedista:Tlapicka"),
    (
        "Commons",
        "https://commons.wikimedia.org/wiki/Special:ListFiles/Tlapicka",
    ),
    ("RSS", "/feeds/all.atom.xml")
    # ("", ""),
)

PROJECTS = [
    {
        "name": "Chytrosti.Marrek.cz",
        "url": "https://chytrosti.marrek.cz/",
        "description": "-- podpora k mé výuce.",
    },
    {
        "name": "OpenZone",
        "url": "https://mamut.spseol.cz/openzone/",
        "description": "-- volnočasové aktivity související se vším, "
        "čím se zabývám.",
    },
    {
        "name": "i3-jinja-config",
        "url": "https://github.com/MarrekNozka/i3-jinja-config",
        "description": "-- konfigurace pro i3wm " " z Jinja2 šablony.",
    },
    {
        "name": "JupyterNotebooks",
        "url": "https://github.com/MarrekNozka/IPythonNotebooks",
        "description": "-- technické výpočty a grafy pomocí MatPlotLib.",
    },
    {
        "name": "pyOdorik",
        "url": "https://github.com/MarrekNozka/pyOdorik",
        "description": "-- klientská CLI aplikace pro snadné "
        "vyhledání kontaktu "
        "a obědnání zpětného volání u VoIP operátora Odorik.cz.",
    },
    {
        "name": "pwscly",
        "url": "https://github.com/MarrekNozka/pwscly",
        "description": "-- CLI aplikace s fuzzy(fzy) vyhledáváním "
        "pro snadnou práci s hesly ve formátu .pwsafe3",
    },
    # {
    #     "name": "",
    #     "url": "",
    #     "description": "",
    # },
]

DEFAULT_PAGINATION = True
DEFAULT_PAGINATION = 12

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {
            "css_class": "highlight",
            "linenums": True,
        },
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": "true", "baselevel": 2},
        "markdown.extensions.admonition": {},
        "mdx_include": {"base_path": PATH},
    },
    "output_format": "html5",
}

PYGMENTS_RST_OPTIONS = {"linenos": "table"}

DOCUTILS_SETTINGS = {
    "smart_quotes": "yes",
    "initial_header_level": 3,
}

STATIC_PATHS = ["extra", "code"]
STATIC_PATHS += ["theme/images", "theme/css", "images", "img", "src", "data"]
EXTRA_PATH_METADATA = {
    "extra/README": {"path": "README.md"},
    "extra/.nojekyll": {"path": ".nojekyll"},
    "extra/CNAME": {"path": "CNAME"},
}

# PIWIK_URL = 'yanek.cz/piwik'
# PIWIK_SITE_ID = 6
