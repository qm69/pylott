#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main file.

Usage:
    main.py <comp> <game> csv-mongo
    main.py <comp> <game> get-last
    main.py -h | --help
    main.py -v | --version

Options:
    <comp>          Company: "unl", "stoloto".
    <game>          Gamen name: "keno", "5x49".
    csv-mongo       Flow from csv to MongoDB.
    get-last        Get last from lottry.com.ua
    -h --help       Show this screen.
    -v --version    Show version.
"""


from docopt import docopt
from termcolor import cprint
# from datetime import datetime
from modules.mongo_db import keno_find, keno_save  # keno_last
from modules.keno_drops import DropCount
from modules.keno_balls import ball_counter
from modules.keno_tenth import part_counter
# from modules.unl_getter import get_keno

args = docopt(__doc__, version='1.14')

"""
Ukraine National Lottery
"""
if args['<comp>'] == "unl":

    ############
    #   KENO   #
    ############
    if args['<game>'] == "keno":

        ###################
        #    csv-mongo    # Schema v.3.5
        ###################
        if args['csv-mongo']:
            """ Keno data model
            firm = 'unl'
            draw = 5943
            date = '12.03.15,
            suit = ['A', '4']
            result = [79, 61, 65, ... , 60, 52, 41]
            sorted = [1, 5, 9, 12 ... , 73, 77, 79]
            """

            with open('results/unl-keno.csv', 'r') as keno_csv:
                # create a list of lists
                # ['5018', '05-01-2015', 'Б', '2', [61, 8, ... 1, 65]
                draw_list = [[[int(n) for n in r.split(",")]
                              if len(r) > 11 else r for r in res.split(";")]
                             for res in keno_csv.read().split('\n')]
                for index, draw in enumerate(draw_list):

                    # cprint(draw_list[0], 'green')
                    draw_numb = int(draw[0], 10)

                    # return Document or None
                    if keno_find('unl', draw_numb) is None:
                        draw_date = draw[1]
                        # from UTF-* bytes to cyrillic 'А' or 'Б'
                        draw_tron = b'\xd0\x90' if draw[2] == 'a' else b'\xd0\x91'
                        draw_ball = draw[4]
                        counter = DropCount(draw_list[index:-30], draw_numb)

                        count = dict(
                            firm='unl',
                            draw=draw_numb,
                            date=draw_date,
                            suit=(draw_tron.decode(), draw[3]),
                            result=draw_ball,
                            sorted=sorted(draw_ball),
                            drop=dict(balls=counter.get_balls(),
                                      # bets=counter.get_odds(),
                                      charts=counter.get_charts()))

                        if index == 0:
                            count["bals"] = ball_counter(draw_list, draw_numb)
                            count["tens"] = part_counter(draw_list, draw_numb)

                        resp = keno_save(count)
                        text_one = 'unl > keno > draw: {} > saved with _id:{}'
                        cprint(text_one.format(draw_numb, resp), 'green')
                    else:
                        text_two = 'unl > keno > draw: {} > exist'
                        cprint(text_two.format(draw_numb), 'red')
                cprint("File 'unl-keno.csv' successfully poured into DB", 'cyan')

        ################
        #   get-last переделать полностью  #
        ################
        elif args['get-last']:
            """
            # 1. get last from unl
            day_today = datetime.now().timetuple().tm_yday + 5013
            resp = get_keno(day_today)
            unl_last = resp if resp["draw"] is not None else get_keno(day_today - 1)
            # cprint(unl_last, 'green')

            # 2. get last from DB
            db_last = keno_last("unl")
            # cprint(db_last, 'cyan')

            # 3. Compare
            if unl_last["draw"] == db_last["draw"]:
                cprint("UNL Keno results is up to date", 'green')

            # 4. Prepend to res csv
            elif unl_last["draw"] > db_last["draw"]:
                arry = list(range(db_last["draw"] + 1,
                                  unl_last["draw"] + 1))
                data_line = ''
                for arr in arry:
                    resp = get_keno(arr)
                    b = [str(resp['n' + str(r)]) for r in list(range(1, 21))]
                    line_ball = ",".join(b)
                    date = '{}-{}-{}'.format(resp["year"], resp["month"], resp["day"])
                    line = '{};{};{};{};{}\n'.format(
                        resp["draw"],
                        date,
                        resp["lototron"],
                        resp["ballset"],
                        line_ball)

                    data_line = line + data_line

                cprint(data_line, 'green')

                with open('results/keno.csv', 'r') as original:
                    data = original.read()
                with open('results/keno.csv', 'w') as modified:
                    modified.write(data_line + data)

                cprint('done', 'green')
            else:
                cprint("4to-to ne tak", 'red')
            """
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
