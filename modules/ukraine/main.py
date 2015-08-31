#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..\\..\\')
from lottlibs.lott_db import LottDB

from now_draw import draw_numb
from get_unl import get_resalts

"""
troika = LottDB('troika')
last_base = troika.find_last('УНЛ')
for_now = draw_numb('troika')
print('Last in base: {}, For now: {}'.format(last_base, for_now))

if for_now == last_base:
    print('Troika is up to date')
else:
    start = 4001 if last_base == 0 else last_base
    for draw in range(start + 1, for_now + 1):
        resp = get_resalts('loto3', draw)
        save = troika.save_one(resp)
        print(save)
"""
decima = LottDB('decima')
last_base = decima.last_draw('УНЛ')
for_now = draw_numb('keno')
print('Last in base: {}, For now: {}'.format(last_base, for_now))

if for_now == last_base:
    print('Keno is up to date')
else:
    start = 5149 if last_base == 0 else last_base
    for draw in range(start + 1, for_now + 1):
        resp = get_resalts('keno', draw)
        save = decima.save_one(resp)
        print(save)
