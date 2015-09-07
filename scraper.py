#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# http://stackoverflow.com/questions/951124
#       /dynamic-loading-of-python-modules

from os import listdir
dirs = [dr for dr in listdir('modules') if not dr.startswith('__')]
print(dirs)
for dr in dirs:
    # __import__(d + '.main' + '.main', fromlist=['']).main()
    path = 'modules.' + dr + '.main'
    modl = __import__('modules.' + dr + '.main', fromlist=[''])
    modl.main()
