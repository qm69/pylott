#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from libs.base_keno_draw import DrawCount

client = MongoClient('localhost', 27017)

db = client['lottmean-dev']
mon_draws = db['kenos']

text_arr = open('results/keno_5053.csv', 'r').read().split('\n')

# make this of lists
# ['5033', '2015-01-20', 'A', '2', '23, ... 35'],
res_arr = [draw.split(';') for draw in text_arr]

for i, res_draw in enumerate(res_arr):

    if i < 10:

        # Split and reverce DATA value
        date_arry = reversed(res_draw[1].split('-'))
        res_balls = res_draw[4].split(',')
        tron_list = [res_draw[2], res_draw[3]]
        count_draw = dict(
            comp='unl',
            draw=int(res_draw[0], 10),
            date='{}.{}.{}'.format(*date_arry),
            tron=tron_list,
            results=res_balls
        )

        # create an array of integer ball resalts
        func = lambda x: [int(ball, 10) for ball in x[4].split(',')]
        int_arr = list(map(func, res_arr[i:30]))

        init_cntr = DrawCount(int_arr, count_draw['draw'])

        count_draw['balls'] = init_cntr.ball_counter()
        count_draw['chart'] = init_cntr.get_chart()
        count_draw['bookies'] = init_cntr.booker()

        res = mon_draws.insert(count_draw)
        print(res)
