#!/usr/bin/env python
# coding=utf8

# redis info
REDIS_HOST = '192.168.1.230'
REDIS_PORT = 6379
REDIS_NUM = 0  # default
REDIS_POOL = 5

# redis conn
KEY_TASK_DOWN_LIST = 'TASK:DOWN'
KEY_TASK_PUSH_LIST = 'TASK:PUSH'

# mongo info
MONGO_HOST = '192.168.1.230'
MONGO_PORT = 27017
MONGO_DB_NAME = 'video'

import web
# disable sessions debug
web.config.debug = False
web.config.session_parameters['timeout'] = 43200
web.config.session_parameters['expired_message'] = 'Session expired'
web.config.session_parameters['ignore_expiry'] = False
web.config.session_parameters['ignore_change_ip'] = True
web.config.session_parameters['cookie_path'] = '/'
