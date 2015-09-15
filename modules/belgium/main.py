#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..\\..\\')
from datetime import date, time, timedelta
from librs.lottdb import LottDB
from librs.printer import print_head, print_save, print_red
from librs.daterange import drange
from librs.actual import draw_date
from modules.belgium.getter import get_resalts


def pick_3():
    triple = LottDB('triple')
    last_draw_in_base = triple.find_last('Belgium', dt=True)
    actl_draw_for_now = draw_date('EU/Belgium', 2.00, True, [time(20, 30)], [0, 1, 2, 3, 4, 5])
    print_head('Belgium. Pick 3',
               last_draw_in_base.date() if last_draw_in_base else 'No resalts',
               actl_draw_for_now)

    if last_draw_in_base == actl_draw_for_now:
        print_red('! results is up to date !')
    else:
        start = last_draw_in_base.date() + timedelta(days=1) if last_draw_in_base else date(2015, 8, 1)
        for draw in drange(start, actl_draw_for_now + timedelta(days=1)):
            rslt = get_resalts('pick_3', draw.strftime('%Y-%m-%d'))
            if rslt:
                save = triple.save_one(rslt)
                print_save(draw, save)
            else:
                print_red('No resalts at ' + draw.strftime('%Y-%m-%d'))


def keno():
    decima = LottDB('decima')
    last_draw_in_base = decima.find_last('Belgium', dt=True)
    actl_draw_for_now = draw_date('EU/Belgium', 2.00, True, [time(20, 30)], [0, 1, 2, 3, 4, 5])
    print_head('Belgium. Keno',
               last_draw_in_base.date() if last_draw_in_base else 'No resalts',
               actl_draw_for_now)

    if last_draw_in_base == actl_draw_for_now:
        print_red('! results is up to date !')

    else:
        start = last_draw_in_base.date() + timedelta(days=1) if last_draw_in_base else date(2015, 8, 1)
        for draw in drange(start, actl_draw_for_now + timedelta(days=1)):
            rslt = get_resalts('keno', draw.strftime('%Y-%m-%d'))
            if rslt:
                save = decima.save_one(rslt)
                print_save(draw, save)
            else:
                print_red('No resalts at ' + draw.strftime('%Y-%m-%d'))


def main():
    pick_3()
    keno()

if __name__ == '__main__':
    main()
