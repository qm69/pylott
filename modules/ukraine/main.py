#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..\\..\\')

from librs.lott_db import LottDB
from librs.printer import print_head, print_save, print_red

from modules.ukraine.actual import draw_numb
from modules.ukraine.getter import get_resalts


def loto3():
    triple = LottDB('triple')
    last_draw_in_base = triple.find_last('УНЛ', draw=True)
    actl_draw_for_now = draw_numb('loto3')
    print_head('УНЛ. Лото Тройка', last_draw_in_base, actl_draw_for_now)

    if last_draw_in_base == actl_draw_for_now:
        print_red('! results is up to date !')
    else:
        for draw in range(last_draw_in_base + 1 if last_draw_in_base else 4050,
                          actl_draw_for_now + 1):
            rslt = get_resalts('loto3', draw)
            save = triple.save_one(rslt)
            print_save(draw, save)


def keno():
    decima = LottDB('decima')
    last_draw_in_base = decima.find_last('УНЛ', draw=True)
    actl_draw_for_now = draw_numb('keno')
    print_head('УНЛ. КЕНО', last_draw_in_base, actl_draw_for_now)

    if last_draw_in_base == actl_draw_for_now:
        print_red('! results is up to date !')
    else:
        for draw in range(last_draw_in_base + 1 if last_draw_in_base else 5200,
                          actl_draw_for_now + 1):
            rslt = get_resalts('keno', draw)
            save = decima.save_one(rslt)
            print_save(draw, save)


def maxima():
    qvinta = LottDB('qvinta')
    last_draw_in_base = qvinta.find_last('УНЛ', draw=True)
    actl_draw_for_now = draw_numb('maxima')
    print_head('УНЛ. Лото Максима', last_draw_in_base, actl_draw_for_now)

    if last_draw_in_base == actl_draw_for_now:
        print_red('! results is up to date !')
    else:
        for draw in range(last_draw_in_base + 1 if last_draw_in_base else 1000,
                          actl_draw_for_now + 1):
            rslt = get_resalts('keno', draw)
            save = qvinta.save_one(rslt)
            print_save(draw, save)


def main():
    loto3()
    keno()
    maxima()

if __name__ == '__main__':
    main()
