#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..\\..\\')

from datetime import time
from librs.lottdb import LottDB
from librs.printer import print_head, print_save, print_red
from librs.actual import draw_numb
from modules.california.getter import past_page


def main_daily_3():
    triple = LottDB('triple')
    last_draw_in_base = triple.find_last('California', 'draw')
    actl_draw_for_now = draw_numb('Pacific Time', -8.00, True, [time(13, 0), time(18, 30)], 12739)
    print_head('California. Daily 3', last_draw_in_base, actl_draw_for_now)

    if last_draw_in_base != actl_draw_for_now:
        daily_draws = past_page('daily_3')
        start = last_draw_in_base + 1 if last_draw_in_base else 13200

        for draw in range(start, actl_draw_for_now + 1):
            if draw in daily_draws.keys():
                rslt = daily_draws[draw]
                save = triple.save_one(rslt)
                print_save(draw, save)
    else:
        print_red('! results is up to date !')


def main_daily_4():
    quatro = LottDB('quatro')
    last_draw_in_base = quatro.find_last('California', 'draw')
    actl_draw_for_now = draw_numb('Pacific Time', -8.00, True, [time(18, 30)], 2418)
    print_head('California. Daily 4', last_draw_in_base, actl_draw_for_now)

    if last_draw_in_base != actl_draw_for_now:
        daily_draws = past_page('daily_4')
        start = last_draw_in_base + 1 if last_draw_in_base else 2659

        for draw in range(start, actl_draw_for_now + 1):
            if draw in daily_draws.keys():
                rslt = daily_draws[draw]
                save = quatro.save_one(rslt)
                print_save(draw, save)
    else:
        print_red('! results is up to date !')


def main():
    # main_daily_3()
    main_daily_4()

if __name__ == '__main__':
    main()
