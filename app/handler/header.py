#!/usr/bin/env python
# -*- coding:utf8 -*-

import web

def addheader():
    web.header('Content-Type', 'application/json; charset=utf-8', unique=True)
    web.header('Cache-Control', 'no-Cache') 
    web.header('Access-Control-Allow-Origin', '*') # 解决js跨域