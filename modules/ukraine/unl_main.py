#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unl_draws import draw_numb
from unl_mongo import Triples
from unl_getter import get_resalts

triples = Triples()
last_base = triples.last_draw('УНЛ')
last_now = draw_numb('troika')

if last_now == last_base:
    print('Up to Date')
else:
    for draw in range(last_base + 1, last_now + 1):
        resp = get_resalts('loto3', draw)
        save = triples.save(resp)
        print(save)
