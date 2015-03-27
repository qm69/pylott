#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main file.

Usage:
    main.py <comp> <game> file-mongo
    main.py <comp> <game> get-last
    main.py -h | --help
    main.py -v | --version

Options:
    <comp>          Company: "unl", "stoloto".
    <game>          Gamen name: "keno", "5x49".
    file-mongo
    balls-parts
    -h --help       Show this screen.
    -v --version    Show version.
"""


from docopt import docopt
from termcolor import cprint
from datetime import datetime
from modules.mongo import keno_find, keno_save, keno_last
from modules.keno_drops import DropCount
from modules.keno_balls import ball_counter
from modules.keno_tenth import part_counter
from modules.unl_getter import get_keno

# 1 game, 3 methods
args = docopt(__doc__, version='0.1.2')

"""
for arg in args:
    print('{} : {}'.format(arg, args[arg]))
"""

if args['<comp>'] == "unl":
    """=============================
    === Ukraine National Lottery ===
    ============================="""
    if args['<game>'] == "keno":

        ###########################
        # unl > keno > file-mongo #
        ###########################
        if args['file-mongo']:
            """ Keno data model
            comp = 'unl'
            draw = 5943
            date = '12.03.15,
            tron = ['A', '4']
            rslt = [79, 61, 65, ... , 60, 52, 41]
            """
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
                for indx, draw in enumerate(draw_list):

                    # cprint(draw_list[0], 'green')
                    draw_numb = int(draw[0], 10)

                    # return Document or None
                    if keno_find('unl', draw_numb) is None:
                        draw_date = '{}.{}.{}'.format(
                            *(reversed(draw[1].split('-')))
                        )
                        draw_tron = (draw[2], draw[3])
                        draw_ball = draw[4]
                        counter = DropCount(draw_list[indx:-30], draw_numb)

                        count = dict(
                            comp='unl',
                            game='keno',
                            draw=draw_numb,
                            date=draw_date,
                            tron=draw_tron,
                            rslt=draw_ball,
                            drop={
                                'balls': counter.get_balls(),
                                'charts': counter.get_charts(),
                                'odds': counter.get_odds()
                            }
                        )
                        if indx == 0:
                            count["balls"] = ball_counter(draw_list, draw_numb)
                            count["tenth"] = part_counter(draw_list, draw_numb)

                        resp = keno_save(count)
                        cprint(
                            'unl > keno > draw: {} > saved with _id:{}'
                            .format(draw_numb, resp), 'green')
                    else:
                        cprint(
                            'unl > keno > draw: {} > exist'
                            .format(draw_numb), 'red')
                cprint("File 'keno.csv' successfully poured into DB", 'cyan')

        ##########################
        # unl > keno > get-last: #
        ##########################
        elif args['get-last']:

            # 1. get last from unl
            day_today = datetime.now().timetuple().tm_yday + 5013
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

            # 4. Prepend to res file
            elif unl_last["draw"] > db_last["draw"]:
                arry = list(range(
                    db_last["draw"] + 1,
                    unl_last["draw"] + 1
                ))
                data_line = ''
                for arr in arry:
                    resp = get_keno(arr)
                    b = [str(resp['n' + str(r)]) for r in list(range(1, 21))]
                    line_ball = ",".join(b)
                    date = '{}-{}-{}'.format(
                        resp["year"], resp["month"], resp["day"])
                    line = '{};{};{};{};{}\n'.format(
                        resp["draw"],
                        date,
                        resp["lototron"],
                        resp["ballset"],
                        line_ball
                    )
                    data_line = line + data_line

                cprint(data_line, 'green')

                with open('results/keno.csv', 'r') as original:
                    data = original.read()
                with open('results/keno.csv', 'w') as modified:
                    modified.write(data_line + data)

                cprint('done', 'green')
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
