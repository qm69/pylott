 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..\\..\\')

from datetime import date, time, timedelta
from librs.lottdb import LottDB
from librs.printer import print_head, print_save, print_red
from librs.actual import draw_date
from librs.dranger import drange
from modules.new_york.getter import NewYork
from termcolor import colored, cprint


def numbers():
    triple = LottDB('triple')
    last_date_in_base, suit_base = triple.find_last('New York', 'date', suit=True)  # or date(2015, 9, 1), 'm'
    actl_draw_for_now, suit_now = draw_date('Eastern Time', -4.00, True, [time(12, 30), time(19, 40)])
    head_text = '\n  New York. Numbers >> {} {} - {} {}'.format(
        last_date_in_base, suit_base, actl_draw_for_now, suit_now)
    print(colored(head_text, 'blue', 'on_white'))

    if last_date_in_base and last_date_in_base == actl_draw_for_now:
        print_red('! results is up to date !')

    else:
        ny = NewYork('win_4', '12', '2015', '2', '2016')
        start = last_date_in_base - timedelta(days=0 if suit_base == 'e' else 1)

        for d_date in drange(start, actl_draw_for_now):
            for s in ['m', 'e']:
                rslt = ny.find(d_date, s)
                if rslt:
                    if rslt['date'].date() == last_date_in_base and rslt['suit'][0] == 'm':
                        print('  Уже должен быть в базе')
                    else:
                        save = triple.save_one(rslt)
                        print_save(d_date, save)


def win_4():
    quatro = LottDB('quatro')
    last_date_in_base, suit_base = quatro.find_last('New York', 'date', suit=True)
    actl_draw_for_now, suit_now = draw_date('Eastern Time', -4.00, True, [time(12, 30), time(19, 40)])

    head_tmpl = '\n  New York. Win 4 >> {} {} - {} {}'
    head_text = head_tmpl.format(last_date_in_base, suit_base, actl_draw_for_now, suit_now)
    print(colored(head_text, 'blue', 'on_white'))

    if last_date_in_base and last_date_in_base == actl_draw_for_now:
        print_red('! results is up to date !')

    else:
        """ диапазано месяцов от 9 до 12"""
        ny = NewYork('win_4', '12', '2015', '2', '2016')
        start = last_date_in_base - timedelta(days=0 if suit_base == 'e' else 1)

        for d_date in drange(start, actl_draw_for_now):
            for s in ['m', 'e']:
                rslt = ny.find(d_date, s)
                if rslt:
                    if rslt['date'].date() == last_date_in_base and rslt['suit'][0] == 'm':
                        print('  Уже должен быть в базе')
                    else:
                        save = quatro.save_one(rslt)
                        print_save(d_date, save)


def main():
    # numbers()
    win_4()

if __name__ == '__main__':
    main()
