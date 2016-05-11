#!/usr/bin/env python
# coding=utf8

import pymongo
import redis
import httplib2
import urllib
import json

http = httplib2.Http()

from config import config  # @UnresolvedImport

def upload(path, data):
    status = 0
    http = httplib2.Http()
    resp, content = http.request(# @UnusedVariable
        '%s/put%s' % (config.MOGILEFS_HOST, path),
        'PUT',
        data
    )
    if resp.status != 201:status = 1
    return status

def clean_cache(keys):
    pass

def preview(mark=0):
    pass

def delete(key):
    pass