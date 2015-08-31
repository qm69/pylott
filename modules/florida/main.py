#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..\\..\\')
from lottlibs.lott_db import LottDB
"""
I: by Url, II: by Date (has no draw numbers)
Florida Lotto => 6 x 53 | Wednesday and Saturday @ 11:15 p.m., Eastern Time.
Powerball     => 5 x 59 + 1 x 35 | Wednesday and Saturday @ 10:59 p.m., Eastern Time.
Mega Millions => 5 x 75 + 1 x 15 | Tuesday and Friday @ 11:00 p.m., Eastern Time.
Lucky Money   => 4 x 47 + 1 x 19 | Tuesday and Friday @ 11:15 p.m., Eastern Time.
Fantasy 5     => 5 x 36 | Daily @ 11:15 p.m. Eastern Time.
Play 4        => 4 x 10 | Midday @ 1:30 p.m. and Evening @ 7:57 p.m. Eastern Time.
Cash 3        => 3 x 10 | Midday @ 1:30 p.m. and Evening @ 7:57 p.m. Eastern Time.
"""
from date_range import date_range
from last_date import last_date
from http_draw import get_draw

quatro = LottDB('quatro')
last_base = quatro.last_date('California')
for_now = last_date('play_4')

print('Last in base: {}, For now: {}'.format(last_base, for_now))

if for_now == last_base:
    print('Keno is up to date')
else:
    for dd in date_range(last_base, for_now):
        resp = get_draw('play_4', dd)
        for draw in resp:
            save = quatro.save_one(draw)
            print(save)
""" PyFuss
#1: решить с датой сместить на -1?
quatro wrap by def func()
"""

if __name__ == '__main__':
	wrap_func()
