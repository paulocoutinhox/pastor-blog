import os
from datetime import datetime

# General
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
USE_THEME = "nid"  # nid or flex

CURRENT_DATETIME = datetime.now().timestamp()

AUTHOR = "Pastor Paulo Coutinho"
SITENAME = "Pastor Paulo Coutinho"
SITETITLE = "Pastor Paulo Coutinho"
SITESUBTITLE = "Meu blog pessoal para compartilhar conhecimento"
SITEDESCRIPTION = "Meu blog pessoal para compartilhar conhecimento"
SITEURL = "http://localhost:8000"
BROWSER_COLOR = "#356689"
ROBOTS = "index, follow"
RELATIVE_URLS = False

if USE_THEME == "nid":
    SITELOGO = "/images/empty.png"
elif USE_THEME == "flex":
    SITELOGO = "/images/logo.png"

TIMEZONE = "America/Sao_Paulo"
DEFAULT_LANG = "pt_BR"
I18N_TEMPLATES_LANG = "en"
LOCALE = "pt_BR"
OG_LOCALE = ["pt_BR"]
DEFAULT_PAGINATION = 30

PATH = "content"
WEBASSETS = True

DEFAULT_OG_IMAGE = "{static}/images/opengraph.png"

DISABLE_URL_HASH = True

PYGMENTS_STYLE = "github"

# Plugins
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

PLUGIN_PATHS = [
    os.path.join(PROJECT_PATH, "vendor", "pelican-plugins"),
    os.path.join(PROJECT_PATH, "plugins"),
]

PLUGINS = [
    "sitemap",
    "extended_meta",
    "related_posts",
    "post_stats",
    "neighbors",
]

if USE_THEME == "nid":
    PLUGINS.append("summary")
    PLUGINS.append("webassets")
elif USE_THEME == "flex":
    PLUGINS.append("i18n_subsites")
    PLUGINS.append("pelican.plugins.search")

# Sitemap
SITEMAP = {"format": "xml"}

# Feed generation (is usually not desired when developing)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Article
ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"

DEFAULT_METADATA = {"status": "published"}

# Related posts
RELATED_POSTS_MAX = 20

# Tag
TAG_URL = "tag/{slug}.html"

# Blogroll
LINKS = (
    ("Galerias de Fotos", "https://galeria.pastorpaulo.com"),
    ("IPDV", "https://www.facebook.com/igrejapdv/"),
)

# Social widget
SOCIAL = (
    ("YouTube", "https://www.youtube.com/channel/UCyRDFfvmXlXmPee29f9_5eQ/videos"),
    ("Twitter", "https://twitter.com/pastorprsvc"),
)

RELATIVE_URLS = False

# Theme
if USE_THEME == "nid":
    THEME = "../nid"
elif USE_THEME == "flex":
    THEME = "vendor/themes/flex"

MENUITEMS = [
    ("Categorias", "/categories.html"),
    ("Tags", "/tags.html"),
    ("Galerias de fotos", "https://galeria.pastorpaulo.com"),
]

if USE_THEME == "nid":
    MENUITEMS.insert(0, ("Início", "/"))

THEME_COLOR = "light"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True
CUSTOM_CSS = "static/css/custom.css"

COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = "Paulo Coutinho"

MAIN_MENU = True
HOME_HIDE_TAGS = True

SHOW_ARTICLE_CATEGORY = True

REL_CANONICAL = True

# Search
if USE_THEME == "flex":
    SEARCH_MODE = "output"
    SEARCH_HTML_SELECTOR = "article div"

# Static files
STATIC_PATHS = ["images", "extras", "static"]

EXTRA_PATH_METADATA = {
    "extras/CNAME": {"path": "CNAME"},
    "extras/robots.txt": {"path": "robots.txt"},
    "extras/ads.txt": {"path": "ads.txt"},
    "extras/favicon/android-chrome-192x192.png": {"path": "android-chrome-192x192.png"},
    "extras/favicon/android-chrome-512x512.png": {"path": "android-chrome-512x512.png"},
    "extras/favicon/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "extras/favicon/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "extras/favicon/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "extras/favicon/favicon.ico": {"path": "favicon.ico"},
    "extras/favicon/site.webmanifest": {"path": "site.webmanifest"},
    "extras/static/css/": {"path": "static/css/"},
    "extras/static/js/": {"path": "static/js/"},
}

if USE_THEME == "nid":
    # use minified css
    NID_MINIFY_CSS = True

    # add header background image from content/images : 'background.jpg'
    NID_HEADER_IMAGES = ""
    NID_HEADER_BANNERS = [
        {"image": "images/banners/banner-biblemania1.jpg", "link": "https://paulocoutinho.pages.dev/biblemania/home/"},
        {"image": "images/banners/banner-curso1.jpg", "link": "https://pay.kiwify.com.br/RDiITGI"},
        {"image": "images/banners/banner-curso2.jpg", "link": "https://pay.kiwify.com.br/RDiITGI"},
    ]
    NID_HEADER_BANNERS_NAVIGATORS = True

    # footer
    NID_SITEMAP_COLUMN_TITLE = "Mapa do site"
    NID_SITEMAP_MENU = [
        ("Arquivos", "/archives.html"),
        ("Tags", "/tags.html"),
        ("Autores", "/authors.html"),
    ]
    NID_SITEMAP_ATOM_LINK = "Atom Feed"
    NID_SITEMAP_RSS_LINK = "RSS Feed"
    NID_SOCIAL_COLUMN_TITLE = "Redes sociais"
    NID_LINKS_COLUMN_TITLE = "Links"
    NID_COPYRIGHT_COLUMN_TITLE = "Copyright"

    # footer optional
    NID_FOOTER_HTML = ""

    # index.html
    NID_INDEX_HEAD_TITLE = "Home"
    NID_INDEX_HEADER_TITLE = "Meu blog pessoal para compartilhar conhecimento"
    NID_INDEX_HEADER_SUBTITLE = "Compartilhando conhecimento"
    NID_INDEX_CONTENT_TITLE = "Últimos posts"
    NID_INDEX_PAGE_NUMBER_TITLE = "Página"

    # archives.html
    NID_ARCHIVES_HEAD_TITLE = "Arquivos"
    NID_ARCHIVES_HEAD_DESCRIPTION = "Arquivos de posts"
    NID_ARCHIVES_HEADER_TITLE = "Arquivos"
    NID_ARCHIVES_HEADER_SUBTITLE = "Arquivos de todos os posts"
    NID_ARCHIVES_CONTENT_TITLE = "Arquivos"

    # article.html
    NID_ARTICLE_HEADER_BY = "Por"
    NID_ARTICLE_HEADER_MODIFIED = "modificado"
    NID_ARTICLE_HEADER_IN = "na categoria"
    NID_ARTICLE_RELATED_TITLE = "Outros conteúdos relacionados"

    # author.html
    NID_AUTHOR_HEAD_TITLE = "Posts de"
    NID_AUTHOR_HEAD_DESCRIPTION = "Posts de"
    NID_AUTHOR_HEADER_SUBTITLE = "Arquivos de posts"
    NID_AUTHOR_CONTENT_TITLE = "Posts"

    # authors.html
    NID_AUTHORS_HEAD_TITLE = "Lista de autor"
    NID_AUTHORS_HEAD_DESCRIPTION = "Lista de autor"
    NID_AUTHORS_HEADER_TITLE = "Lista de autor"
    NID_AUTHORS_HEADER_SUBTITLE = "Arquivos listados por autor"

    # categories.html
    NID_CATEGORIES_HEAD_TITLE = "Categorias"
    NID_CATEGORIES_HEAD_DESCRIPTION = "Arquivos listados por categoria"
    NID_CATEGORIES_HEADER_TITLE = "Categorias"
    NID_CATEGORIES_HEADER_SUBTITLE = "Arquivos listados por categoria"

    # category.html
    NID_CATEGORY_HEAD_TITLE = "Arquivo de categoria"
    NID_CATEGORY_HEAD_DESCRIPTION = "Arquivo de categoria"
    NID_CATEGORY_HEADER_TITLE = "Categoria"
    NID_CATEGORY_HEADER_SUBTITLE = "Arquivo de categoria"

    # pagination.html
    NID_PAGINATION_PREVIOUS = "Anterior"
    NID_PAGINATION_NEXT = "Próximo"

    # period_archives.html
    NID_PERIOD_ARCHIVES_HEAD_TITLE = "Arquivos de"
    NID_PERIOD_ARCHIVES_HEAD_DESCRIPTION = "Arquivos de"
    NID_PERIOD_ARCHIVES_HEADER_TITLE = "Arquivos"
    NID_PERIOD_ARCHIVES_HEADER_SUBTITLE = "Arquivos de"
    NID_PERIOD_ARCHIVES_CONTENT_TITLE = "Arquivos de"

    # tag.html
    NID_TAG_HEAD_TITLE = "Arquivo de tags"
    NID_TAG_HEAD_DESCRIPTION = "Arquivo de tags"
    NID_TAG_HEADER_TITLE = "Tag"
    NID_TAG_HEADER_SUBTITLE = "Arquivo de tags"

    # tags.html
    NID_TAGS_HEAD_TITLE = "Tags"
    NID_TAGS_HEAD_DESCRIPTION = "Lista de tags"
    NID_TAGS_HEADER_TITLE = "Tags"
    NID_TAGS_HEADER_SUBTITLE = "Lista de tags"
    NID_TAGS_CONTENT_TITLE = "Lista de tags"
    NID_TAGS_CONTENT_LIST = "marcado"
    NID_TAGS_SINGLE_ARTICLE_TITLE = "artigo"
    NID_TAGS_SEVERAL_ARTICLES_TITLE = "artigos"
