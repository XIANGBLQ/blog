# -*- coding: utf-8 -*-
#: settings for liquidluck

#: site information
#: all variables can be accessed in template with ``site`` namespace.
#: for instance: {{site.name}}
site = {
    "name": "Hello, World!",  # your site name
    "url": "http://terryoy.github.io/",  # your site url
    # "prefix": "blog",
    "friendly_links": [
        {
            "name": u'中文博客',
            "link": 'http://terryoy.github.io/thoughts/',
        }
    ],
    "google_adsense": "ca-pub-6012718593977391",
    "google_adslot_nav": "1828084194",
    "google_adslot_post": "1086396907",
}

#: this config defined information of your site
#: 1. where the resources  2. how should the site be generated
config = {
    "source": "../_content",
    "output": "../docs",
    "static": "../docs/static",
    "static_prefix": "/static/",
    "permalink": "{{date.year}}/{{date.month}}/{{filename}}.html",
    "relative_url": False,
    "perpage": 30,
    "feedcount": 20,
    "timezone": "+08:00",
}


author = {
    "default": "terryoy",
    "vars": {}
}

#: active readers
reader = {
    "active": [
        "liquidluck.readers.markdown.MarkdownReader",
        # uncomment to active rst reader.
        # but you need to install docutils by yourself
        # "liquidluck.readers.restructuredtext.RestructuredTextReader",
    ],
    "vars": {}
}

#: active writers
writer = {
    "active": [
        "liquidluck.writers.core.PostWriter",
        "liquidluck.writers.core.PageWriter",
        "liquidluck.writers.core.ArchiveWriter",
        "liquidluck.writers.core.ArchiveFeedWriter",
        "liquidluck.writers.core.FileWriter",
        "liquidluck.writers.core.StaticWriter",
        "liquidluck.writers.core.YearWriter",
        "liquidluck.writers.core.CategoryWriter",
        "liquidluck.writers.core.CategoryFeedWriter",
        "liquidluck.writers.core.TagWriter",
        "liquidluck.writers.core.TagCloudWriter",
    ],
    "vars": {
        # uncomment if you want to reset archive page
        # "archive_output": "archive.html",
    }
}

#: theme variables
theme = {
    "name": "minimal",

    # theme variables are defined by theme creator
    # you can access theme in template with ``theme`` namespace
    # for instance: {{theme.disqus}}
    "vars": {
        "author": "terryoy",
        "disqus": "terryoy",
        #"analytics": "UA-21475122-1",

        'navigation': [
			{'name': 'Home', 'link': '/'},
            {'name': 'Guides', 'link':'/guides/index.html'},
            {'name': 'Tricks', 'link':'/tricks/index.html'},
            {'name': '*Projects', 'link': '/projects.html'},
			{'name': 'About Me', 'link': '/about.html'},
        ]
    }
}

#: template variables
template = {
    "vars": {},
    "filters": {},
}
