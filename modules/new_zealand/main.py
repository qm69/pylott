#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..\\..\\')

from librs.lott_db import LottDB
from librs.printer import print_head, print_save, print_red

from modules.new_zealand.actual import draw_numb
from modules.new_zealand.getter import get_resalts


def play_3():
    triple = LottDB('triple')
    last_draw_in_base = triple.find_last('New Zealand', draw=True)
    actl_draw_for_now = draw_numb('play_3')
    print_head('New Zealand. Play 3', last_draw_in_base, actl_draw_for_now)

    if last_draw_in_base == actl_draw_for_now:
        print_red('! results is up to date !')

    else:
        start = last_draw_in_base + 1 if last_draw_in_base else 299
        for draw in range(start, actl_draw_for_now + 1):
            rslt = get_resalts('play_3', draw)
            save = triple.save_one(rslt)
            print_save(draw, save)


def main():
    play_3()

if __name__ == '__main__':
    main()
