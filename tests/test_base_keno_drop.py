#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $ py.test -v [--maxfail=1] test_base_keno_drop.py

import sys
import pytest

# http://stackoverflow.com/questions/714063/
sys.path.append('/home/qm69/code/python/lottery')

from pylott.modules.base_keno_drop import DropCount
from pylott.results.keno_list_1000 import draw_list

get_balls = pytest.mark.get_balls
get_charts = pytest.mark.get_charts
get_odds = pytest.mark.get_odds

# $ py.test -v -m get_balls
# $ py.test -v -m "not get_odds"
# $ py.test -v -m "get_balls or get_charts"


@pytest.fixture(scope="module")
def dc():
    return DropCount(draw_list[:30], 5053)


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
            assert ball['hot'] in ['hot', 'cold', 'neit']

            # 2 Odd or Even
            assert ball['even'] in ['odd', 'even']

            # 3 More or Less
            assert ball['half'] in ['first', 'last']

            # 4 First, Second, Third or Fourth
            twenty_val = ['first', 'second', 'third', 'fourth']
            assert ball['twenty'] in twenty_val

            # 5 Once, Twice, Threce, Fource or More
            rep_val = ['once', 'twice', 'threce', 'fource', 'fifce', 'sixce']
            assert ball['repeat'] in rep_val

            # 6 Active, Passive or Neit
            assert ball['active'] in ['active', 'passive', 'neit']

            # 7 Rise or Fall
            assert ball['rise'] in ['rise', 'fall', 'neit']

    @get_charts
    def test_drop_get_charts(self, dc):
        resp = dc.get_charts()

        assert type(resp) is dict
        assert len(resp) == 8

        # evens
        assert sum(resp['evens'][1:]) == 20

        # halves
        assert sum(resp['halves'][1:]) == 20

        # twentys
        assert sum(resp['twentys'][1:]) == 20

        # tenth
        assert sum(resp['tenth'][1:]) == 20

    @get_odds
    def test_drop_get_odds(self, dc):
        resp = dc.get_odds()

        # totals of second half < 610
        assert type(resp['totals'][0]) is int
        assert resp['totals'][0] > 0
        assert resp['totals'][0] <= 610

        # totals of second half < 1331
        assert type(resp['totals'][1]) is int
        assert resp['totals'][1] > 0
        assert resp['totals'][1] <= 1331

        # totals of first and second halfs == total totals
        totals = resp['totals'][0] + resp['totals'][1]
        assert totals == resp['totals'][2]

        for k, v in resp.items():
            if (k != 'totals'):
                assert v[0] > 0
                assert v[0] < 81
                assert v[1] != ''
                assert v[2] != ''
