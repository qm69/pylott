#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main file.

Usage:
    main.py <comp> <game> csv-to-mongo
    main.py <comp> <game> drops (-l=<last> | -d=<draw>)
    main.py <comp> <game> balls (-l=<last> | -d=<draw>)
    main.py <comp> <game> tenth (-l=<last> | -d=<draw>)
    main.py <comp> <game> today
    main.py -h | --help
    main.py -v | --version

Options:
    -h --help       Show this screen.
    -v --version    Show version.
    <comp>          Company: "unl", "stoloto".
    <game>          Gamen name: "keno", "5x49".
    -l=<last>       Emount of last draws.
    -d=<draw>       Number of draws.

"""

from docopt import docopt
from modules.db import keno_draw, save_keno
# from modules.keno_drop import DropCount
# from modules.keno_ball import ball_counter
# from modules.keno_part import part_counter

args = docopt(__doc__, version='0.1.7')

if args['<comp>'] == "unl":
    if args['<game>'] == "keno":
        if args['csv-to-mongo']:
            """ Keno data model
            comp = 'unl'
            draw = 5943
            date = '12.03.15,
            tron = ['A', '4']
            rslt = [79, 61, 65, ... , 60, 52, 41]
            """
            line_data_list = open('results/keno.csv', 'r').read().split('\n')

            for line_data in line_data_list:

                #   ['5018', '2015-01-05', 'B', '2', [61, 8, ... 1, 65]
                draw_data = [
                    [int(n) for n in r.split(",")]
                    if len(r) > 11 else r
                    for r in line_data.split(";")
                ]
                draw_numb = int(draw_data[0], 10)
                draw_date = '{}.{}.{}'.format(
                    *(reversed(draw_data[1].split('-')))
                )
                draw_tron = (draw_data[2], draw_data[3])
                draw_ball = draw_data[4]
                cont_draw = dict(
                    comp='unl',
                    game='keno',
                    draw=draw_numb,
                    date=draw_date,
                    tron=draw_tron,
                    rslt=draw_ball
                )
                print(draw_numb)
                #   if draw number in base
                if keno_draw(cont_draw) is not True:
                    resp = save_keno(cont_draw)
                    print('{} saved'.format(resp))
                else:
                    print('Тираж {} в базе'.format(draw_numb))

            print('Well done!')

        # unl keno last ...
        elif args['last']:
            """
            1. идет по по скрипту и забирает результаты
            2. прогоняет через DropCount, ball_counter, part_counter
            3. PROFIT
            """
            pass

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

"""
# ['5033', '2015-01-20', 'A', '2', '23, .., 35'],
rslt_list = [draw.split(';') for draw in text_arr]

# получить массив из массивов результатов в виде целых чисел
# [ ... [23, 20, 11, .., 49, 9, 32], ... ]
resalt = [[int(x) for x in res[4].split(',')] for res in rslt_list]
"""
