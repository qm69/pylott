#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main file.

Usage:
    main.py <comp> <game> csv-to-db
    main.py <comp> <game> drops [-l=<last>]
    main.py <comp> <game> balltenth [-d=<draw>]

    main.py <comp> <game> draw [-d=<draw>]
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
from modules.mongo import keno_fone, keno_save, keno_updt
from modules.keno_drop import DropCount
from modules.keno_ball import ball_counter
from modules.keno_part import part_counter

args = docopt(__doc__, version='0.1.7')

"""
for arg in args:
    print('{} : {}'.format(arg, args[arg]))

<comp> : unl
<game> : keno
csv-to-mongo : False
balltenth : False
drops : True
today : False
-l : 1

--version : False
--help : False
"""

if args['<comp>'] == "unl":
    """'''''''''''''''''''''''''''''
    ''' Ukraine National Lottery '''
    '''''''''''''''''''''''''''''"""
    if args['<game>'] == "keno":

        ##########################
        # unl > keno > csv-to-db #
        ##########################
        if args['csv-to-db']:
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
                    # return Document or None
                    if keno_fone(cont_draw) is None:
                        resp = keno_save(cont_draw)
                        print('{} saved'.format(resp))
                    else:
                        # print('Тираж {} в базе'.format(draw_numb))
                        pass
                print('Well done!')

        #######################
        # unl > keno > drops: #
        #######################
        elif args['drops']:
            # line_data_list = open('results/keno.csv', 'r')
            # .read().split('\n')
            with open('results/keno.csv', 'r') as keno_file:
                # print(keno_file.read().split("\n"))
                # create a list of lists like
                # ['5018', '2015-01-05', 'B', '2', [61, 8, ... 1, 65]
                draw_list = [
                    [
                        [int(n) for n in r.split(",")]
                        if len(r) > 11 else r for r in res.split(";")
                    ]
                    for res in keno_file.read().split('\n')
                ]
                length = 0
                for indx, draw in enumerate(draw_list):
                    # print(args['-l'], 'asdadasdas')
                    if indx < int(args['-l']):

                        # TODO: проверку на наличие doc["draw"]
                        draw_numb = int(draw[0])
                        counter = DropCount(draw_list[indx:-30], draw_numb)
                        dropped = {
                            'balls': counter.get_balls(),
                            'charts': counter.get_charts(),
                            'odds': counter.get_odds()
                        }

                        # by db.kenos.findAndModify
                        # return full Document
                        resp = keno_updt(
                            draw_numb, comp="unl",
                            type="drop", data=dropped
                        )
                        print(resp)

        ########################
        # unl > keno > balltenth:
        #########################
        elif args['balltenth']:
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

                draw_numb = int(draw_list[0][0])
                bc = ball_counter(draw_list, draw_numb)
                pc = part_counter(draw_list, draw_numb)
                resp = keno_updt(draw_numb, comp="unl", type="balls", data=bc)
                pesp = keno_updt(draw_numb, comp="unl", type="tenth", data=pc)
                print(len(resp))
                print(len(pesp))

        # unl -> keno -> today:
        elif args['today']:
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
