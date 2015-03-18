#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main file.

Usage:
    main.py <comp> <game> last [-l=<least>]
    main.py <comp> <game> draw (-d=<draws> | -s=<start> -e=<end>)
    main.py <comp> <game> cron
    main.py -h | --help
    main.py -v | --version

Options:
    -h --help       Show this screen.
    -v --version    Show version.
    <comp>          Company: "unl", "stoloto"
    <game>          Gamen name: "keno", "5x49"
    -l=<draw>       Least numbers from the last.
    -s=<start>      Start.
    -e=<end>        End.

$ python3 main.py unl maxima draw -s 34 -e 100
    --help: False
    --version: False
    draw: True
    cron: False
    last: False
    unl: maxima
    <game> maxima
    <comp> unl
    -e 100
    -l None
    -s 34
"""

from docopt import docopt

args = docopt(__doc__, version='0.1.7')

print(args['<comp>'], args['<game>'])
for arg in args:
    print(arg, args[arg])

if args['<comp>'] == "unl":
    if args['<game>'] == "keno":
        if args['last']:
            pass
        elif args['draw']:
            pass
        elif args['cron']:
            pass
        else:
            # raise Exception
            print("Не равильная команда из 'draw', 'last' or 'cron'")

    elif args['<game>'] == "super":
        pass
    elif args['<game>'] == "maxima":
        pass
    else:
        # raise Exception
        print("Не правильно введена игра")
elif args['<comp>'] == "stoloto":
    pass
else:
    # raise Exception
    print("Не правильно написано имя компании")
