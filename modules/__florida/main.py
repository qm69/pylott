#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..\\..\\')
from datetime import date, timedelta

from librs.lottdb import LottDB
from librs.printer import print_head, print_save, print_red
from librs.date_range import drange

from modules.__florida.actual import draw_date
from modules.__florida.getter import get_resalts

"""
I: by Url, II: by Date (has no draw numbers)
Eastern Time => зимой (ноябрь-март) - UTC-5,  летом (апрель-октябрь) — UTC-4
Florida Lotto => 6 x 53          | Wednesday and Saturday @ 23:15 [+1 day 03:15 GMT, +1 day 06:15 Kiev]
Powerball     => 5 x 59 + 1 x 35 | Wednesday and Saturday @ 22:59 [+1 day 02:59 GMT, +1 day 05:59 Kiev]
Mega Millions => 5 x 75 + 1 x 15 | Tuesday and Friday @ 23:00 [+1 day 03:00 GMT, +1 day 06:00 Kiev]
Lucky Money   => 4 x 47 + 1 x 19 | Tuesday and Friday @ 23:15 [+1 day 03:15 GMT, +1 day 06:15 Kiev]
Fantasy 5     => 5 x 36          | Daily @ 23:15 [+1 day 03:15 GMT, +1 day 06:15 Kiev]
Play 4        => 4 x 10          | Midday @ 13:30 [17:57 GMT, +1 day 20:30 Kiev] and
                                   Evening @ 19:57 [23:57 GMT, +1 day 02:57 Kiev]
Cash 3        => 3 x 10          | Midday @ 13:30 [17:57 GMT, +1 day 20:30 Kiev] and
                                   Evening @ 19:57 [23:57 GMT, +1 day 02:57 Kiev]
"""


def cash_3():
    triple = LottDB('triple')
    # dt.datetime
    last_draw_in_base = triple.find_last('Florida', dt=True)
    print(last_draw_in_base)
    # dt.date
    actl_draw_for_now = draw_date('cash_3')

    print_head('Florida. Cash 3', last_draw_in_base, actl_draw_for_now)

    if last_draw_in_base and last_draw_in_base == actl_draw_for_now:
        print_red('! results is up to date !')
    else:
        start = last_draw_in_base.date() + timedelta(days=1) if last_draw_in_base else date(2015, 8, 1)
        for draw in drange(start, actl_draw_for_now):
            rslt = get_resalts('cash_3', draw)
            if len(rslt) == 1:
                save = triple.save_one(rslt)
                print_save(draw, save)
            elif len(rslt) == 2:
                [print_save(draw, triple.save_one(rs)) for rs in rslt]
            else:
                print_red('No resalts at ' + draw.strftime('%Y-%m-%d'))


def play_4():
    quatro = LottDB('quatro')
    last_draw_in_base = quatro.find_last('Florida', dt=True)
    actl_draw_for_now = draw_date('play_4')
    print_head('Florida. Play 4',
               last_draw_in_base.date() if last_draw_in_base else 'No resalts',
               actl_draw_for_now)

    if last_draw_in_base.date() == actl_draw_for_now:
        print_red('  ! results is up to date !')
    else:
        start = last_draw_in_base + timedelta(days=1) if last_draw_in_base else date(2015, 8, 1)
        for draw in drange(start, actl_draw_for_now + timedelta(days=1)):
            rslt = get_resalts('play_4', draw)
            if len(rslt) == 1:
                save = quatro.save_one(rslt)
                print_save(draw, save)
            elif len(rslt) == 2:
                [print_save(draw, quatro.save_one(rs)) for rs in rslt]
            else:
                print_red('No resalts at ' + draw.strftime('%Y-%m-%d'))


def main():
    cash_3()
    # play_4()

if __name__ == '__main__':
    main()
