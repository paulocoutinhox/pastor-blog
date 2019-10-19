# -*- coding: utf-8 -*- #
"""
Open Graph
==========
This plugin adds Open Graph Protocol tags to articles.
Use like this in your base.html template:
.. code-block:: jinja2
  {% if article %}
  {% for tag in article.ogtags %}
  <meta property="{{tag[0]}}" content="{{tag[1]|striptags|e}}" />
  {% endfor %}
  {% endif %}
  {% if page  %}
  {% for tag in page.ogtags %}
  <meta property="{{tag[0]}}" content="{{tag[1]|striptags|e}}" />
  {% endfor %}
  {% endif %}
"""
from __future__ import unicode_literals

import os.path

from pelican import generators, signals
from pelican.utils import strftime
from bs4 import BeautifulSoup
from jinja2 import Markup


def open_graph_tag_articles(content_generators):

    for generator in content_generators:
        if isinstance(generator, generators.ArticlesGenerator):
            for article in (
                generator.articles + generator.translations + generator.drafts
            ):
                open_graph_tag(article)
        elif isinstance(generator, generators.PagesGenerator):
            for page in generator.pages:
                open_graph_tag(page)

    return True


def open_graph_tag(item):
    ogtags = []

    ogtags.append(("og:title", item.title))
    ogtags.append(("twitter:title", item.title))
    ogtags.append(("og:type", "article"))
    ogtags.append(("twitter:card", "summary"))

    image = item.metadata.get("og_image", "")

    if image:
        ogtags.append(("og:image", image))
        ogtags.append(("twitter:image", image))
    else:
        soup = BeautifulSoup(item._content, "html.parser")
        img_links = soup.find_all("img")
        img_src = ""

        if len(img_links) > 0:
            img_src = img_links[0].get("src")
        else:
            if item.settings.get("DEFAULT_OG_IMAGE", ""):
                img_src = item.settings.get("DEFAULT_OG_IMAGE", "")

        if img_src:
            if img_src.startswith("{attach}"):
                img_path = os.path.dirname(item.source_path)
                img_filename = img_src[8:]
                img_src = os.path.join(img_path, img_filename)

                if item.settings.get("SITEURL", ""):
                    img_src = item.settings.get("SITEURL", "") + "/" + img_src
            elif img_src.startswith(("{filename}", "|filename|")):
                img_src = img_src[11:]

                if item.settings.get("SITEURL", ""):
                    img_src = item.settings.get("SITEURL", "") + "/" + img_src
            elif img_src.startswith("{static}"):
                img_src = img_src[9:]

                if item.settings.get("SITEURL", ""):
                    img_src = item.settings.get("SITEURL", "") + "/" + img_src
            elif img_src.startswith("/static"):
                img_src = img_src[8:]

                if item.settings.get("SITEURL", ""):
                    img_src = item.settings.get("SITEURL", "") + "/" + img_src
            elif img_src.startswith("data:image"):
                pass
            elif not "http" in img_src:
                if item.settings.get("SITEURL", ""):
                    img_src = item.settings.get("SITEURL", "") + "/" + img_src

        if img_src:
            ogtags.append(("og:image", img_src))
            ogtags.append(("twitter:image", img_src))

    url = os.path.join(item.settings.get("SITEURL", ""), item.url)
    ogtags.append(("og:url", url))

    default_summary = Markup(item.summary).striptags()
    description = Markup.escape(item.metadata.get("og_description", default_summary))
    ogtags.append(("og:description", description))
    ogtags.append(("twitter:description", description))

    default_locale = item.settings.get("LOCALE", [])

    if default_locale:
        default_locale = default_locale[0]
    else:
        default_locale = ""

    ogtags.append(("og:locale", item.metadata.get("og_locale", default_locale)))
    ogtags.append(("og:site_name", item.settings.get("SITENAME", "")))
    ogtags.append(("twitter:site", item.settings.get("SITENAME", "")))

    if hasattr(item, "date"):
        ogtags.append(("article:published_time", strftime(item.date, "%Y-%m-%d")))

    if hasattr(item, "modified"):
        ogtags.append(("article:modified_time", strftime(item.modified, "%Y-%m-%d")))

    if hasattr(item, "related_posts"):
        for related_post in item.related_posts:
            url = os.path.join(item.settings.get("SITEURL", ""), related_post.url)
            ogtags.append(("og:see_also", url))

    author_fb_profiles = item.settings.get("AUTHOR_FB_ID", {})

    if len(author_fb_profiles) > 0:
        for author in item.authors:
            if author.name in author_fb_profiles:
                ogtags.append(("article:author", author_fb_profiles[author.name]))

    ogtags.append(("article:section", item.category.name))

    if hasattr(item, "tags"):
        for tag in item.tags:
            ogtags.append(("article:tag", tag.name))

    item.ogtags = ogtags


def register():
    signals.all_generators_finalized.connect(open_graph_tag_articles)
