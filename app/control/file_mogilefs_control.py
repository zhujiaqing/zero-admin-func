#!/usr/bin/python
# coding=utf8

import json
import web
import time

from handler import header  # @UnresolvedImport
from service import file_mogilefs_service  # @UnresolvedImport

class upload:
    def __init__(self):
        header.addheader()
        
    def POST(self):
        res = {'ret':0}
        try:
            file_path = web.input().get('path')
            file_path.replace(' ', '')
            
            upload = web.input(uploadFile={})['uploadFile']
            file_name = upload.filename
            
            if 0 == len(file_name) or 0 == len(upload.file.read()):raise Exception
            
            if file_path is None or 0 == len(file_path):
                file_path = '/upload/' + time.strftime('%y/%m/%d/%H/%M/%S/') + file_name
            file_path = str(file_path)
            
            status = file_mogilefs_service.upload(file_path, upload.file.read())
            
            if status != 0:
                res['ret'] = 1
                info = '上传失败'
            else:
                info = '上传成功'
                addrs = [
                    'http://yj.cdndown.youja.cn/get%s' % file_path,
                    'http://ws.cdndown.youja.cn/get%s' % file_path,
                    'http://yp.cdndown.youja.cn/get%s' % file_path,
                    'http://al.cdndown.youja.cn/get%s' % file_path
                ]
                res['addrs'] = addrs
            
            res['info'] = info
            res['name'] = file_name
            res['path'] = file_path
        except:
            res = {'ret':1, 'info':'上传过程出现异常'}
            
        return json.dumps(res)

class clean_cache:
    def __init__(self):
        header.addheader()
        
    def POST(self):
        res = {'ret':0}
        try:
            keys = web.input().get('keys')
            keys = keys.split('\n')
            file_mogilefs_service.clean_cache(keys)
            res['keys'] = keys
        except:
            res['ret'] = 1
            res['info'] = '清除缓存失败'
        
        return json.dumps(res)

class preview:
    def __init__(self):
        header.addheader()
        
    def POST(self):
        res = {'ret':0}
        try:
            pass
        except:
            res['ret'] = 1
            res['info'] = '获取列表失败'
            
        return json.dumps(res)
    
class delete:
    def __init__(self):
        header.addheader()
        
    def POST(self):
        res = {'ret':0}
        try:
            pass
        except:
            res['ret'] = 1
            res['info'] = '删除失败'
            
        return json.dumps(res)
