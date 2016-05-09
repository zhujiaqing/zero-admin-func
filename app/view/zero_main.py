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
        web.setcookie("name", "jesse", 20, None, None, None, "/")
        return json.dumps(res)
    
    
