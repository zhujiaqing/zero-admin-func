#!/usr/bin/python
# coding=utf8

import web
from url import urls
from config import config  # @UnusedImport

app = web.application(urls.urls, globals())
session = web.session.Session(app, web.session.DiskStore('/tmp/sessions'), initializer={'count': 0})

if __name__ == "__main__":
    app.run()
