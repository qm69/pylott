#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..\\..\\')
from datetime import time
from librs.lottdb import LottDB
from librs.printer import print_head, print_save, print_red
from librs.actual import draw_numb
from modules.new_zealand.getter import get_resalts


def play_3():
    triple = LottDB('triple')
    last_draw_in_base = triple.find_last('New Zealand', draw=True)
    actl_draw_for_now = draw_numb('New Zealand', 12.00, True, [time(18, 0)], 87)
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
