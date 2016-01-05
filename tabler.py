#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Usage:
    main.py once
    main.py twice
    main.py triple <firm>
    main.py quatro <firm>
    main.py qvinta <firm>
    main.py sextra <firm>
    main.py decima <firm>
    main.py -h | --help
    main.py -v | --version

Options:
    once           Once per Day
    twice          Twice per Day
    triple <firm>  3 x 10
    quatro <firm>  4 x 10
    qvinta <firm>  5 x n
    sextra <firm>  6 x n
    decima <firm>  20 x 80
    <firm>         "УНЛ", "Belgium", "California".
    -h --help     Show this screen.
    -v --version  Show version.
"""

from docopt import docopt
from librs.tablelibs.triple import triple
from librs.tablelibs.quatro import quatro
from librs.tablelibs.decima import decima

args = docopt(__doc__, version='1.14')
firm = args['<firm>']
# game_type = args['<game_type>']

if args['once']:
    print('\n  УНЛ  >>  Тройка')
    triple('УНЛ')
    print('\n  УНЛ  >>  Кено')
    decima('УНЛ')
    print('\n  Belgium  >>  Pick 3')
    triple('Belgium')
    print('\n  California  >>  Daily 4')
    quatro('California')
    print('\n  New Zealand  >>  Play 3')
    triple('New Zealand')

if args['twice']:
    print('\n  California  >>  Daily 3')
    triple('California')
    print('\n  Florida  >>  Ca$h 3')
    triple('Florida')
    print('\n  Florida  >>  Play 4')
    quatro('Florida')
    print('\n  New York  >>  Win 4')
    quatro('New York')

# Вид лотереи
if args['triple']:
    triple(firm)

if args['quatro']:
    quatro(firm)

if args['decima']:
    decima(firm)

if args['qvinta']:
    print('  Section does not ready yet.')

if args['sextra']:
    print('  Section does not ready yet.')
