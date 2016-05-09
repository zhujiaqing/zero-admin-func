#!/usr/bin/python
# coding = utf8

from view import file_mogilefs  # @UnresolvedImport
from view import zero_main  # @UnresolvedImport

urls = (
    r'/zero_admin/login', zero_main.login,
    r'/zero_admin/mfs/upload', file_mogilefs.upload,
)
