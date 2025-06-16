AUTHOR = "PyJax"
SITENAME = "PyJax"
SITEURL = ""

ATTRIBUTION = True

PATH = "content"
STATIC_PATHS = ["images", "files"]

TIMEZONE = "America/New_York"

# FILENAME_METADATA = r"(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US.UTF-8"

THEME = "pelican-themes/alchemy/alchemy"
THEME_CSS_OVERRIDES = ["theme/css/oldstyle.css"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
)

# Social widget
SOCIAL = (
    ("meetup", "https://www.meetup.com/py-jax/"),
    ("github", "https://github.com/pyjax/"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PAGE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}"

ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"

AUTHOR_SAVE_AS = "author/{slug}/index.html"
AUTHOR_URL = "author/{slug}/"

CATEGORY_SAVE_AS = "category/{slug}/index.html"
CATEGORY_URL = "category/{slug}/"

TAG_SAVE_AS = "tag/{slug}/index.html"
TAG_URL = "tag/{slug}/"

# PLUGIN_PATHS = ["pelican-plugins"]
# PLUGINS = ["sitemap"]

# Theme specific - alchemy
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = []

SITESUBTITLE = ""
DESCRIPTION = "PyJax is a forum for Python programming enthusiasts around Jacksonville"
