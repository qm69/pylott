#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main file.

Usage:
    main.py <comp> <game> csv-to-mongo
    main.py <comp> <game> drops [-l=<last>]
    main.py <comp> <game> balltenth [-l=<last>]
    main.py <comp> <game> today
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
from modules.db import keno_draw, keno_save, keno_updt
from modules.keno_drop import DropCount
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
            with open('results/keno.csv', 'r') as keno_file:

                for line_data in keno_file.read().split('\n'):

                    # ['5018', '2015-01-05', 'B', '2', [61, 8, ... 1, 65]
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
                    # print(draw_numb)
                    # check for draw number in base
                    if keno_draw(cont_draw) is not True:
                        resp = keno_save(cont_draw)
                        print('{} saved'.format(resp))
                    else:
                        # print('Тираж {} в базе'.format(draw_numb))
                        pass
                print('Well done!')

        # unl keno last ...
        elif args['drops']:
            # line_data_list = open('results/keno.csv', 'r')
            # .read().split('\n')
            with open('results/keno.csv', 'r') as keno_file:

                # create a list of lists like
                # ['5018', '2015-01-05', 'B', '2', [61, 8, ... 1, 65]
                draw_list = [
                    [
                        [int(n) for n in r.split(",")]
                        if len(r) > 11 else r for r in res.split(";")
                    ]
                    for res in keno_file.split('\n')
                ]
                for indx, draw in enumerate(draw_list):
                    if indx < int(args['<game>']):

                        draw_numb = int(draw[0])
                        """
                        1.  Написать фунц в 'db.py' которая по "draw" и "comp"
                            находит и возвращает обект.
                        2.  Переписать "DropCount" который теперь получает
                            не массив только из тиражей, а полностью
                            или тутже эго обрезать и замапить [x for x in ...]
                        3.  Прикручивает к обекту поле ["drop"] из
                                "balls", "charts" & "odds"
                        4.  Сохраняет результат
                        """
                        count_draw = {}
                        ball_list = []  # пункт два замапить сюда
                        init_cntr = DropCount(
                            ball_list[indx:30],
                            draw_numb
                        )

                        count_draw['balls'] = init_cntr.get_balls()
                        count_draw['test_ball'] = init_cntr.get_charts()
                        count_draw['totals'] = init_cntr.get_odds()

                        resp = keno_updt(count_draw)
                        print(resp)

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
