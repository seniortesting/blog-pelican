#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# 详细的配置文件
AUTHOR = u'Walter Hu'
SITENAME = 'PingBook Blog'
SITESUBTITLE ='import __hello__ import this'
SITEURL = 'https://pingbook.top'
SITE_THUMBNAIL = '/static/images/profile.jpg'
SITE_THUMBNAIL_TEXT = 'Might come with a beard'

# 时间设置
TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
    'zh_CN': '%Y-%m-%d %H:%M:%S',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
SLUGIFY_SOURCE = 'basename'  # 使用文件名作用url路径
DEFAULT_DATE = 'fs'  # use filesystem's mtime
# LOCALE = ('zh_CN.utf8',)
DEFAULT_LANG = u'zh_CN'
# Do not publish articles set in the future
WITH_FUTURE_DATES = False
MARKDOWN = {
    'extension_configs': {
        # https://pythonhosted.org/Markdown/extensions/index.html#officially-supported-extensions
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.meta': {},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.smarty': {},
        'markdown.extensions.toc': {'permalink': True},
        # https://facelessuser.github.io/pymdown-extensions/
        'pymdownx.extra': {},
        'pymdownx.caret': {'superscript': True},
        'pymdownx.magiclink': {},
        'pymdownx.smartsymbols': {},
    },
    'output_format': 'html5',
    # Allow numbered lists to not start with 1. Used in following article:
    # https://kevin.deldycke.com/2016/12/falsehoods-programmers-believe-about-falsehoods-lists/
    # See: https://pythonhosted.org/Markdown/reference.html#lazy_ol
    'lazy_ol': False,
}


# GITHUB_URL = 'http://github.com/pingbook'
TYPOGRIFY = True
PDF_GENERATOR = False
# 归档和目录的列表的显示排序
NEWEST_FIRST_ARCHIVES =True
REVERSE_CATEGORY_ORDER = True
# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_MAX_ITEMS = 20
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'  #为分类添加Feed
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# 菜单
MENUITEMS = (
    ('Home', '/'),
    ('Category', '/categories'),
    ('Archive', '/archives'),
    ('Tags', '/tags')
)
DIRECT_TEMPLATES = ('index', 'archives', 'categories', 'tags', 'authors', 'search')  # 直接生成的页面的列表,不用加上 .html 的扩展名.

# 生成的对应目录
PAGE_URL = '{slug}'
ARTICLE_URL = 'articles/{slug}/'
CATEGORY_URL = 'category/{slug}/'
TAGS_URL = 'tags'
TAG_URL = 'tag/{slug}/'
AUTHORS_URL ='authors'
AUTHOR_URL ='author/{slug}'
# 产生的文件的路径
PAGE_SAVE_AS = '{slug}/index.html'
INDEX_SAVE_AS = 'index.html'
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
# 归档整理
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}.html'
MONTH_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/{date:%b}/index.html'
# Deactivate author URLs
AUTHOR_SAVE_AS = 'author/{slug}'
AUTHORS_SAVE_AS = 'authors/index.html'
TEMPLATE_PAGES = {
    "404.html": "404.html",
}

# 友情链接
LINKS = (
         ('我的博客园', 'http://www.cnblogs.com/alterhu/'),
         ('[运维]Xiao Hanyu', 'http://xiaohanyu.me/about/'),
         ('[前端]黄玄的博客', 'http://huangxuan.me/'),
         ('[前端]阮一峰', 'http://www.ruanyifeng.com/blog/'),
         ('[Python]Data Engineer','https://kevin.deldycke.com/')
         )

# 媒体设置
SOCIAL = (
          ('gmail', 'mailto:alterhu2020@gmail.com?subject=From PingBook question'),
          ('twitter', 'https://twitter.com/alterhu2020'),
          ('github', 'http://github.com/pingbook')
         )
DISQUS_SITENAME = "pingbook"

# 路径设置
PATH = 'content'
ARTICLE_PATHS = ['articles']
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True
DEFAULT_CATEGORY = 'uncategorized'
DEFAULT_PAGINATION = 10


PAGE_PATHS = ['pages']
# 静态资源的路径,相当于 PATH
STATIC_PATHS = ['static','extra/robots.txt', 'extra/CNAME', 'extra/favicon.ico', 'extra/baidu_verify_TVrRxDNlTJ.html','extra/google9db45b3da980c919.html']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/baidu_verify_TVrRxDNlTJ.html': {'path': 'baidu_verify_TVrRxDNlTJ.html'},
    'extra/google9db45b3da980c919.html': {'path': 'google9db45b3da980c919.html'}
}
# STATIC_CHECK_IF_MODIFIED = True
RELATIVE_URLS = True

# 缓存配置
CACHE_CONTENT = True
CONTENT_CACHING_LAYER = 'reader'
CACHE_PATH = 'cache'
GZIP_CACHE = True
LOAD_CONTENT_CACHE = True

# 主题和插件
THEME = './pelican-themes/gum'
PLUGIN_PATHS = [u"pelican-plugins"]
PLUGINS = [
    "better_codeblock_line_numbering",
    "gzip_cache",
    "neighbors",
    "related_posts",
    "sitemap",
    "tag_cloud",
    "tipue_search"
]
# 压缩
GZIP_CACHE_OVERWRITE =False
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
# read more 插件
# SUMMARY_MAX_LENGTH = 150
# 相关文章
RELATED_POSTS_MAX =6

# 标签云
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 30
TAG_CLOUD_SORTING = 'alphabetically'
TAG_CLOUD_BADGE = True

# 谷歌广告
GOOGLE_ANALYTICS_ID = 'UA-122219517-1'
GOOGLE_ADSENSE={
    'ca_id': 'ca-pub-1893384651266286',    # Your AdSense ID
    'page_level_ads': True,          # Allow Page Level Ads (mobile)
    'ads': {
        'aside': '1234561',          # Side bar banner (all pages)
        'article_top': '1234565',    # Banner after article title (article only)
        'article_bottom': '1234566', # Banner after article content (article only)
    }
}