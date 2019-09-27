#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

# General
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

AUTHOR = "Pastor Paulo Coutinho"
SITENAME = "Pastor Paulo Coutinho"
SITESUBTITLE = "Meu blog pessoal para compartilhar conhecimento"
SITEURL = ""
SITEDESCRIPTION = "Meu blog pessoal para compartilhar conhecimento"

RELATIVE_URLS = False

TIMEZONE = "America/Sao_Paulo"
DEFAULT_LANG = "pt-br"
I18N_TEMPLATES_LANG = "pt_BR"
LOCALE = ["pt_BR"]
DEFAULT_PAGINATION = 20

PATH = "content"
WEBASSETS = True

# Plugins
PLUGIN_PATHS = [
    os.path.join(PROJECT_PATH, "vendor"),
    os.path.join(PROJECT_PATH, "plugins"),
]

PLUGINS = ["assets", "sitemap", "summary", "extended_meta"]

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

# Tag
TAG_URL = "tag/{slug}.html"

# Blogroll
LINKS = (
    ("IPDV", "https://www.facebook.com/igrejapdv/"),
    ("PRSoluções", "https://prsolucoes.com/"),
)

# Social widget
SOCIAL = (
    ("YouTube", "https://www.youtube.com/channel/UCyRDFfvmXlXmPee29f9_5eQ/videos"),
    ("Twitter", "https://twitter.com/pastorprsvc"),
)

RELATIVE_URLS = False

# Nid Template
THEME = "nid"
MENUITEMS = [
    ("Início", "/"),
    ("Categorias", "/categories.html"),
    ("Tags", "/tags.html"),
]

# use minified CSS
NID_CSS_MINIFY = True

# add header background image from content/images : 'background.jpg'
NID_HEADER_IMAGES = ""
NID_HEADER_LOGO = "/images/logo.png"
NID_REL_CANONICAL_LINK = True

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
NID_COPYRIGHT = "&copy; Pastor Paulo Coutinho 2019"

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
NID_ARCHIVES_HEADER_SUBTITLE = "Arquivos de todas os posts"
NID_ARCHIVES_CONTENT_TITLE = "Arquivos"

# article.html
NID_ARTICLE_HEADER_BY = "Por"
NID_ARTICLE_HEADER_MODIFIED = "modificado"
NID_ARTICLE_HEADER_IN = "na categoria"

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

# Static files
STATIC_PATHS = ["images", "extras"]

EXTRA_PATH_METADATA = {
    "extras/CNAME": {"path": "CNAME"},
    "extras/robots.txt": {"path": "robots.txt"},
    "extras/favicon/android-chrome-192x192.png": {"path": "android-chrome-192x192.png"},
    "extras/favicon/android-chrome-512x512.png": {"path": "android-chrome-512x512.png"},
    "extras/favicon/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "extras/favicon/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "extras/favicon/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "extras/favicon/favicon.ico": {"path": "favicon.ico"},
    "extras/favicon/site.webmanifest": {"path": "site.webmanifest"},
}
