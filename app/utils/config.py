#!/usr/bin/env python
# coding=utf8

import web

# session
web.config.session_parameters['cookie_name'] = 'jsid'
web.config.session_parameters['cookie_domain'] = None
web.config.session_parameters['timeout'] = 100,  # 24 * 60 * 60, # 24 hours   in seconds
web.config.session_parameters['ignore_expiry'] = True
web.config.session_parameters['ignore_change_ip'] = True
web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
web.config.session_parameters['expired_message'] = 'Session expired'


# redis info
REDIS_HOST = 'ops.redis.youja.cn'
REDIS_PORT = 6610
REDIS_NUM = 5  # default
REDIS_POOL = 5

# mongo info
MONGO_HOST = 'master.mongo.youja.cn'
MONGO_PORT = 27017
MONGO_DB_NAME = 'ops'

# mogilefs 
MOGILEFS_HOST = 'http://fs.uplus.youja.cn'
