#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main file.

Usage:
    main.py <comp> <game> file-mongo
    main.py <comp> <game> drops [<last>]
    main.py <comp> <game> last
    main.py -h | --help
    main.py -v | --version

Options:
    <comp>          Company: "unl", "stoloto".
    <game>          Gamen name: "keno", "5x49".
    file-mongo
    drops
    <last>          Emount of last draws.
    balls-parts
    -h --help       Show this screen.
    -v --version    Show version.
"""


from docopt import docopt
from termcolor import cprint
from datetime import datetime
from modules.mongo import keno_find, keno_save, keno_updt, keno_last
from modules.keno_drops import DropCount
from modules.keno_balls import ball_counter
from modules.keno_tenth import part_counter
from modules.unl_getter import get_keno

# 1 game, 3 methods
args = docopt(__doc__, version='0.1.3')

"""
for arg in args:
    print('{} : {}'.format(arg, args[arg]))
"""

if args['<comp>'] == "unl":
    """=============================
    === Ukraine National Lottery ===
    ============================="""
    if args['<game>'] == "keno":

        ##########################
        # unl > keno > csv-to-db #
        ##########################
        if args['file-mongo']:
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

                    # return Document or None
                    if keno_find('unl', draw_numb) is None:
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
                        resp = keno_save(cont_draw)
                        cprint(
                            'unl > keno > draw: {} > saved with _id:{}'
                            .format(draw_numb, resp), 'green')
                    else:
                        cprint(
                            'unl > keno > draw: {} > exist'
                            .format(draw_numb), 'red')
                cprint("File 'keno.csv' successfully poured into DB", 'cyan')

        #######################
        # unl > keno > drops: #
        #######################
        elif args['drops']:

            with open('results/keno.csv', 'r') as keno_file:
                # create a list of lists like
                # ['5018', '2015-01-05', 'B', '2', [61, 8, ... 1, 65]
                draw_list = [
                    [
                        [int(n) for n in r.split(",")]
                        if len(r) > 11 else r for r in res.split(";")
                    ]
                    for res in keno_file.read().split('\n')
                ]

                # args['<last>'] = None || '1234'
                emount = len(draw_list) \
                    if (args["<last>"] is None) \
                    else int(args["<last>"])

                for indx, draw in enumerate(draw_list):
                    draw_numb = int(draw[0])
                    if indx < emount:
                        # проверка есть ли "drop" в документе
                        if not ("drop" in keno_find("unl", draw_numb).keys()):

                            counter = DropCount(draw_list[indx:-30], draw_numb)
                            dropped = {
                                'balls': counter.get_balls(),
                                'charts': counter.get_charts(),
                                'odds': counter.get_odds()
                            }

                            # return full Document as dictionary
                            resp = keno_updt(
                                draw_numb,
                                comp="unl",
                                type="drop",
                                data=dropped)

                            cprint(
                                'unl > keno > draw: {} > ["drop"] > saved'
                                .format(resp["draw"]), 'green')
                        else:
                            cprint(
                                'unl > keno > draw: {} > ["drop"] > exist'
                                .format(draw_numb), 'red')

        ######################
        # unl > keno > last: #
        ######################
        elif args['last']:

            # 1. get last from unl
            day_today = datetime.now().timetuple().tm_yday
            resp = get_keno(day_today)
            unl_last = resp \
                if resp["draw"] is not None \
                else get_keno(day_today - 1)
            # cprint(unl_last, 'green')

            # 2. get last from DB
            db_last = keno_last("unl")
            # cprint(db_last, 'cyan')

            # 3. Compare
            if unl_last["draw"] == db_last["draw"]:
                cprint("Up to date", 'green')
            elif unl_last["draw"] > db_last["draw"]:
                arry = list(range(
                    db_last["draw"] + 1,
                    unl_last["draw"] + 1
                ))
                print(arry)
                with open('results/keno.csv', 'r') as keno_file:
                    
            
            else:
                cprint("4to-to ne tak", 'red')

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
