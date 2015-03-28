#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $ py.test -v [--maxfail=1] test_keno_drop.py
# $ py.test -v -m get_balls
# $ py.test -v -m "not get_odds"
# $ py.test -v -m "get_balls or get_odds"

import sys
import pytest

# http://stackoverflow.com/questions/714063/
sys.path.append('/home/qm69/code/python/lottery')

from pylott.modules.keno_drops import DropCount
with open('results/keno.csv', 'r') as keno_file:

    # create a list of lists like
    # ['5018', '2015-01-05', 'B', '2', [61, 8, ... 1, 65]
    draw_list = [
        [
            [int(n) for n in r.split(",")]
            if len(r) > 11 else r for r in res.split(";")
        ]
        for res in keno_file.read().split('\n')
    ]

    get_balls = pytest.mark.get_balls
    get_charts = pytest.mark.get_charts
    get_odds = pytest.mark.get_odds

    @pytest.fixture(scope="module")
    def dc():
        last_draw = int(draw_list[0][0])
        return DropCount(draw_list[:-30], last_draw)

    class TestClass:

        @get_balls
        def test_drop_get_balls(self, dc):
            resp = dc.get_balls()

            # test the whole list
            assert type(resp) is list
            assert len(resp) == 20

            # test each ball from list
            for ball in resp:
                assert type(ball) is dict
                assert len(ball) == 9

                # 1 Hot or Cold
                assert ball['temp'] in ['hot', 'cold', 'neit']

                # 2 Odd or Even
                assert ball['even'] in ['odd', 'even']

                # 3 More or Less
                assert ball['half'] in ['first', 'last']

                # 4 First, Second, Third or Fourth
                twenty_val = ['first', 'second', 'third', 'fourth']
                assert ball['twen'] in twenty_val

                # 5 Once, Twice, Threce, Fource or More
                rep_val = [
                    'once', 'twice', 'threce',
                    'fource', 'fifce', 'sixce'
                ]
                assert ball['rept'] in rep_val

                # 6 Active, Passive or Neit
                assert ball['actv'] in ['active', 'passive', 'neit']

                # 7 Rise or Fall
                assert ball['rise'] in ['rise', 'fall', 'neit']

        @get_charts
        def test_drop_get_charts(self, dc):
            resp = dc.get_charts()

            assert type(resp) is dict
            assert len(resp) == 7

            # evens
            assert sum(resp['even'][1:]) == 20

            # halves
            assert sum(resp['half'][1:]) == 20

            # twentys
            assert sum(resp['twel'][1:]) == 20

        @get_odds
        def test_drop_get_odds(self, dc):
            resp = dc.get_odds()

            # totals of second half < 610
            assert type(resp['totl'][0]) is int
            assert resp['totl'][0] > 0
            assert resp['totl'][0] <= 610

            # totals of second half < 1331
            assert type(resp['totl'][1]) is int
            assert resp['totl'][1] > 0
            assert resp['totl'][1] <= 1331

            # totals of first and second halfs == total totals
            totals = resp['totl'][0] + resp['totl'][1]
            assert totals == resp['totl'][2]

            for k, v in resp.items():
                if (k != 'totl'):
                    assert v[0] > 0
                    assert v[0] < 81
                    assert v[1] != ''
                    assert v[2] != ''
