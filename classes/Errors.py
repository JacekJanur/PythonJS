# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:28:03 2021

@author: adoso
"""
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ConnectionExist(Error):
    """Raised when adding connection exists"""
    pass

class ConnectionNotExist(Error):
    """Raised when deleting connection doesnt exist"""
    pass