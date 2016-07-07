#!/usr/bin/python
# coding = utf8

from controls import file_control  # @UnresolvedImport

app_url = (
    r'/file/get', file_control.file_get,
    r'/file/upload/put', file_control.upload_put,
    r'/file/cdn/cache', file_control.cdn_cache,
)
