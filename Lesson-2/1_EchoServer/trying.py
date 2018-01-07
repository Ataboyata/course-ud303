# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 10:15:25 2018

@author: Arturo
"""

from urllib.parse import urlparse, parse_qs
address = 'https://www.google.com/search?q=gray+squirrel&tbm=isch'
parts = urlparse(address)
print(parts)
