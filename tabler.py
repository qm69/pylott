#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

About.

Usage:
    main.py <game> <comp>
    main.py -h | --help
    main.py -v | --version

Options:
    <game>        "triple", "quatro", "decima"
    <comp>        Like: "УНЛ", "California".
    -h --help     Show this screen.
    -v --version  Show version.
"""

from docopt import docopt
from librs.tablelibs.triple import triple
from librs.tablelibs.quatro import quatro
from librs.tablelibs.decima import decima

args = docopt(__doc__, version='1.14')
game_type = args['<game>']
comp = args['<comp>']

"""
Ukraine National Lottery
"""

if game_type == 'triple':
    triple(comp)
elif game_type == 'quatro':
    quatro(comp)
elif game_type == 'decima':
    decima(comp)
else:
    print('There is no such Mongo collection')
