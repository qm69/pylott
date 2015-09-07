#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..\\..\\')
from libraries.lott_db import LottDB
from termcolor import cprint, colored
from modules.belgium.actual import draw_date
from modules.belgium.getter import get_resalts
from modules.belgium.drange import date_range
from datetime import timedelta, date


def print_head(title, last_base, actual):
    print(colored('\n  ' + title, 'blue', 'on_white'))
    print(colored('  in base: ', 'green') +
          colored(last_base, 'red') +
          colored(', actual: ', 'green') +
          colored(actual, 'red'))


def print_save(draw, save):
    print(colored('  saved: ', 'green') +
          colored(draw, 'red') +
          colored(', id: ', 'green') +
          colored(str(save)[-6:], 'red'))


def pick_3():
    triple = LottDB('triple')
    last_draw_in_base = triple.find_last('Belgium', dt=True)
    actl_draw_for_now = draw_date('pick_3')
    print_head('Belgium. Pick 3',
               last_draw_in_base.date() if last_draw_in_base else 'No resalts',
               actl_draw_for_now)

    if last_draw_in_base == actl_draw_for_now:
        cprint('  ! results is up to date !', 'red')
    else:
        start = last_draw_in_base.date() + timedelta(days=1) if last_draw_in_base else date(2015, 8, 1)
        for draw in date_range(start, actl_draw_for_now + timedelta(days=1)):
            rslt = get_resalts('pick_3', draw.strftime('%Y-%m-%d'))
            if rslt:
                save = triple.save_one(rslt)
                print_save(draw, save)
            else:
                cprint('  No resalts at ' + draw.strftime('%Y-%m-%d'), 'red')


def keno():
    decima = LottDB('decima')
    last_draw_in_base = decima.find_last('Belgium', dt=True)
    actl_draw_for_now = draw_date('keno')
    print_head('Belgium. Keno',
               last_draw_in_base.date() if last_draw_in_base else 'No resalts',
               actl_draw_for_now)

    if last_draw_in_base == actl_draw_for_now:
        cprint('  ! results is up to date !', 'red')
    else:
        start = last_draw_in_base.date() + timedelta(days=1) if last_draw_in_base else date(2015, 8, 1)
        for draw in date_range(start, actl_draw_for_now + timedelta(days=1)):
            rslt = get_resalts('keno', draw.strftime('%Y-%m-%d'))
            if rslt:
                save = decima.save_one(rslt)
                print_save(draw, save)
            else:
                cprint('  No resalts at ' + draw.strftime('%Y-%m-%d'), 'red')


def main():
    pick_3()
    keno()

if __name__ == '__main__':
    main()
