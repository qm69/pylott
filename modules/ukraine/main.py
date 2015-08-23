#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..\\..\\')
from lottlibs.mongo_db import Troika
from unl_draws import draw_numb
from unl_getter import get_resalts

troika = Troika()
last_base = troika.last_draw('УНЛ')
last_now = draw_numb('troika')

if last_now == last_base:
    print('Up to Date')
else:
    for draw in range(last_base + 1, last_now + 1):
        resp = get_resalts('loto3', draw)
        save = troika.save(resp)
        print(save)
