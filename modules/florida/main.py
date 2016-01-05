#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..\\..\\')
from datetime import date, time, timedelta

from librs.lottdb import LottDB
from librs.printer import print_head, print_save, print_red
from librs.dranger import drange
from librs.actual import draw_date
from modules.florida.getter import get_resalts


def cash_3():
    triple = LottDB('triple')
    # suit=True >> [datetime.date(2015, 9, 8), 'e']
    last_date_in_base, suit_base = triple.find_last('Florida', 'date', suit=True)
    # suit=True >> [datetime.date(2015, 9, 8), 'm']
    actl_draw_for_now, suit_now = draw_date('EastTime', -4.00, True, [time(13, 30), time(19, 57)])

    print_head('Florida. Cash 3', last_date_in_base, actl_draw_for_now)
    if last_date_in_base and last_date_in_base == actl_draw_for_now:
        print_red('! results is up to date !')

    else:
        asdf = 0 if suit_base == 'e' else 1
        for draw in drange(last_date_in_base - timedelta(days=asdf), actl_draw_for_now):
            rslt = get_resalts('cash_3', draw)
            if rslt:
                for r in rslt:
                    """
                    !!! !!! передеалать
                    """
                    if r['date'].date() == last_date_in_base and r['suit'][0] == 'M':
                        print('  Уже должен быть в базе')
                    else:
                        save = triple.save_one(r)
                        print_save(draw, save)
            else:
                print_red('No resalts at ' + draw.strftime('%Y-%m-%d'))


def play_4():
    """ {
        "game": "Play 4",
        "resalt": [3, 8, 7, 3],
        "firm": "Florida",
        "date": { "$date": "2015-11-01T19:30:00.000Z" },
        "suit": ["m"]
    } """
    quatro = LottDB('quatro')
    # suit=True >> [datetime.date(2015, 9, 8), 'e']
    last_date_in_base, suit_base = quatro.find_last('Florida', 'date', suit=True) or [date(2015, 9, 8), 'e']
    # suit=True >> [datetime.date(2015, 9, 8), 'm']
    actl_draw_for_now, suit_now = draw_date('EastTime', -4.00, True, [time(13, 30), time(19, 57)])

    print_head('Florida. Play 4', last_date_in_base, actl_draw_for_now)
    if last_date_in_base and last_date_in_base == actl_draw_for_now:
        print_red('! results is up to date !')

    else:
        asdf = 0 if suit_base == 'e' else 1
        for draw in drange(last_date_in_base - timedelta(days=asdf), actl_draw_for_now):
            rslt = get_resalts('play_4', draw)
            if rslt:
                for r in rslt:
                    # проверить чтоб из первой пары не сохраял 'M'
                    if r['date'].date() == last_date_in_base and r['suit'][0] == 'M':
                        print('  Уже должен быть в базе')
                    else:
                        save = quatro.save_one(r)
                        print_save(draw, save)
            else:
                print_red('No resalts at ' + draw.strftime('%Y-%m-%d'))


def main():
    cash_3()
    play_4()

if __name__ == '__main__':
    main()
