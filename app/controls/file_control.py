#!/usr/bin/python
# coding=utf8

import web

from utils import header  # @UnresolvedImport

render = web.template.render('templates')

class file_get:
    def __init__(self):
        header.html()
        
    def GET(self):
        msg = {'ret':2}
        return render.file_get(msg)

class upload_put:
    def __init__(self):
        header.html()

    def POST(self):
        msg = {'ret':2}
        return render.file_get(msg)

class cdn_cache:
    def __init__(self):
        header.html()

    def POST(self):
        msg = {'ret':2}
        return render.file_get(msg)
