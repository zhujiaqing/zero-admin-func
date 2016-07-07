#!/usr/bin/env python
# -*- coding:utf8 -*-

import web

def json():
    web.header('Content-Type', 'application/json; charset=utf-8', unique=True)
    web.header('Cache-Control', 'no-Cache') 
    web.header('Access-Control-Allow-Origin', '*')  # 解决js跨域
    
def html():
    web.header('Content-Type', 'text/html; charset=utf-8', unique=True)
    web.header('Cache-Control', 'no-Cache') 
    
