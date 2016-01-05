#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# http://stackoverflow.com/questions/951124
#       /dynamic-loading-of-python-modules

from os import listdir
# ["belgium", "california", .., "ukraine"]
dirs = [dr for dr in listdir('modules') if not dr.startswith('__')]

for fold in dirs:
    """
    modules.belgium.main
    modules.ukraine.main
    modules.new_zealand.main
    """
    # path = 'modules.' + fold + '.main'
    modl = __import__('modules.' + fold + '.main', fromlist=[''])
    modl.main()
