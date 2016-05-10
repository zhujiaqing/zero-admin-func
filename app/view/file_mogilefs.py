#!/usr/bin/python
# coding=utf8

import json
import web
import time
import httplib2

from handler import header  # @UnresolvedImport

class upload:
    def __init__(self):
        header.addheader()
        
    def POST(self):
        res = {'ret':0}
        try:
            file_path = web.input().get('path')
            file_path.replace(' ', '')
            
            x = web.input(uploadFile={})
            file_name = x['uploadFile'].filename
            
            if file_path is None or 0 == len(file_path):
                file_path = '/upload/' + time.strftime('%y/%m/%d/%H/%M/%S/') + file_name
            file_path = str(file_path)
            
            http = httplib2.Http()
            resp, content = http.request(# @UnusedVariable
                'http://fs.uplus.youja.cn/put%s' % file_path,
                'PUT',
                x['uploadFile'].file.read()
            )
            
            if resp.status != 201:
                res['ret'] = 1
                info = '上传失败'
            else:
                info = '上传成功'
                addr = ['http://yj.cdndown.youja.cn/get%s' % file_path,
                    'http://ws.cdndown.youja.cn/get%s' % file_path,
                    'http://yp.cdndown.youja.cn/get%s' % file_path,
                    'http://al.cdndown.youja.cn/get%s' % file_path]
                res['addr'] = addr
            
            res['info'] = info
            res['name'] = file_name
            res['path'] = file_path
        except:
            res = {'ret':1, 'info':'请求参数存在问题'}
            
        return json.dumps(res)
    
    
    
