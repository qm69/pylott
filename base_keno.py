#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from modules.keno_drop import DropCount
from modules.keno_ball import ball_counter
from modules.keno_part import part_counter

client = MongoClient('localhost', 27017)

db = client['lottmean-dev']
mong_draw = db['draws']
mong_drop = db['drops']
mong_ball = db['balls']
mong_part = db['parts']

text_arr = open('results/keno_last.csv', 'r').read().split('\n')

# ['5033', '2015-01-20', 'A', '2', '23, .., 35'],
res_arr = [draw.split(';') for draw in text_arr]

# [ ... [23, 20, 11, .., 49, 9, 32], ... ]
ball_list = [[int(x) for x in res[4].split(',')] for res in res_arr]

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

        init_cntr = DropCount(ball_list[i:30], int(res_arr[0][0]))

        count_draw['balls'] = init_cntr.get_balls()
        count_draw['test_ball'] = init_cntr.get_charts()
        count_draw['totals'] = init_cntr.get_odds()

        res = mong_drop.insert(count_draw)
        print(res)

""" ball stats counting """
bc = ball_counter(ball_list, res_arr[0][0])
for b in bc:
    resp = mong_ball.insert(b)
    print(resp)


""" part stats counting """
pc = part_counter(ball_list, res_arr[0][0])
for p in pc:
    resp = mong_part.insert(p)
    print(resp)
