#!/usr/bin/python
# coding=utf8

import json
import web

from handler import header  # @UnresolvedImport

class login:
    def __init__(self):
        header.addheader()
        
    def POST(self):
        res = {'ret':0}
        print web.cookies()
        i = web.input()
        web.setcookie("loginusr", i.get("loginusr", ""), 30, None, None, None, "/")
#         return json.dumps(res)
        raise web.seeother("/")
    
    
