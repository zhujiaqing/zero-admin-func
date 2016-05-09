#!/usr/bin/python
# coding=utf8

import json
import web

from handler import header  # @UnresolvedImport
from service import file_mogilefs  # @UnresolvedImport

class upload:
    def __init__(self):
        header.addheader()
        
    def POST(self):
        res = {'ret':0}
        x = web.input(myfile={})
        web.debug(x['myfile'].filename) # 这里是文件名
        web.debug(x['myfile'].value) # 这里是文件内容
        web.debug(x['myfile'].file.read()) # 或者使用一个文件对象
        file_mogilefs.upload()
        return json.dumps(res)
    
    
    
