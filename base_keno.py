#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from libs.base_keno_draw import DrawCount

client = MongoClient('localhost', 27017)
db = client['draw-base']
# посмотреть вместо collection = db['test-collection']
mon_draws = db.test_keno

text_arr = open('results/keno_5053.csv', 'r').read().split('\n')

# make this of lists['5033', '2015-01-20', 'A', '2', '23, ... 35'],
res_arr = [draw.split(';') for draw in text_arr]

for i, res_draw in enumerate(res_arr):

    if i < 10:

        # Split and reverce DATA value
        date_arry = reversed(res_draw[1].split('-'))
        res_balls = [int(ball, 10) for ball in res_draw[4].split(',')]
        count_draw = dict(
            firma='unl',
            tirag=int(res_draw[0], 10),
            date='{}.{}.{}'.format(*date_arry),
            tron=res_draw[2],
            nabor=res_draw[3],
            # create TUPLE to prevent sorting
            results=res_balls
        )
        # create an array of integer ball resalts
        f = lambda x: [int(ball, 10) for ball in x[4].split(',')]
        int_arr = list(map(f, res_arr[i:30]))

        init_cntr = DrawCount(int_arr, count_draw['tirag'])

        count_draw['balls'] = init_cntr.ball_counter()
        count_draw['chart'] = init_cntr.get_chart()
        count_draw['bookies'] = init_cntr.booker()

        res = mon_draws.insert(count_draw)
        print(res)
