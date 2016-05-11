#!/usr/bin/python
# coding = utf8

from control import zero_main_control  # @UnresolvedImport
from control import file_mogilefs_control  # @UnresolvedImport

urls = (
    r'/zero_admin/login', zero_main_control.login,
    
    r'/zero_admin/mfs/upload', file_mogilefs_control.upload,
    r'/zero_admin/mfs/clean_cache', file_mogilefs_control.clean_cache,
    r'/zero_admin/mfs/preview', file_mogilefs_control.preview,
    r'/zero_admin/mfs/delete', file_mogilefs_control.delete,
    
    
)
