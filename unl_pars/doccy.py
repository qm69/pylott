#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main file.

Usage:
    main.py <comp> <game> file-mongo
    main.py <comp> <game> drops [<last>]
    main.py -h | --help
    main.py -v | --version

Options:
    -h --help       Show this screen.
    -v --version    Show version.
    <comp>          Company: "unl", "stoloto".
    <game>          Gamen name: "keno", "5x49".
    -l=<last>       Emount of last draws.

"""

from docopt import docopt

args = docopt(__doc__, version='0.1.7')
"""
for arg in args:
    print('{}: {}'.format(arg, args[arg]))

a if test else b
"""
arry = [1, 2, 3, 4, 54, 6, 4, 3, 3, 4, 4, 5, 6, 7, 9]

asdf = len(arry) if (args["<last>"] is None) else int(args["<last>"])
print(asdf)
