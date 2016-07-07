#!/usr/bin/python
# coding=utf8

import web
import time

from utils import urls

web.config.debug = False

app = web.application(urls.app_url, globals())

db = web.database(dbn='sqlite', db='/tmp/s-%s.db' % int(time.time()))
db.query('''
 create table sessions (
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
);
''')
store = web.session.DBStore(db, 'sessions')
session = web.session.Session(app, store, initializer={'count': 100, 'info': 'js'})


def session_hook():
    web.ctx.session = session

app.add_processor(web.loadhook(session_hook))

if __name__ == "__main__":
    app.run()
