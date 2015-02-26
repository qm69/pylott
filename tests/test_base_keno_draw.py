#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $ py.test -v test_base_keno_draw.py

import sys
import pytest

# http://stackoverflow.com/questions/714063/
sys.path.append('/home/qm69/code/python/lottery')

from pylott.modules.base_keno_draw import DrawCount
from pylott.results.keno_list_1000 import draw_list

"""
@pytest.fixture(scope="module")
@pytest.fixture(scope="session")
@pytest.fixture(
    scope="function",
    params=["mod1", "mod2"]
)
"""


@pytest.fixture(scope="module")
def dc():
    return DrawCount(draw_list[:30], 5053)


class TestClass:

    @classmethod
    def setup_class(cls):
        pass

    def test_get_balls(self, dc):
        resp = dc.get_balls()

        # test the whole list
        assert type(resp) is list
        assert len(resp) == 20

        # test each ball from list
        for ball in resp:
            assert type(ball) is dict

            # 1 Hot or Cold
            assert ball['hot'] in ['hot', 'cold', 'neit']

            # 2 Odd or Even
            assert ball['odd'] in ['odd', 'even']

            # 3 More or Less
            assert ball['more'] in ['more', 'less']

            # 4 First, Second, Third or Fourth
            twenty_val = ['first', 'second', 'third', 'fourth']
            assert ball['twenty'] in twenty_val

            # 5 Once, Twice, Threce, Fource or More
            rep_val = ['once', 'twice', 'threce', 'fource', 'fifce', 'sixce']
            assert ball['vypad'] in rep_val

            # 6 Active, Passive or Neit
            assert ball['active'] in ['active', 'passive', 'neit']

            # 7 Rise or Fall
            assert ball['rise'] in ['rise', 'fall', 'neit']

    def test_get_charts(self, dc):
        resp = dc.get_charts()

        # 'odd'
        assert sum(resp['odd'][1:]) == 20

        # 'more'
        assert sum(resp['more'][1:]) == 20

        # 'twenty'
        assert sum(resp['twenty'][1:]) == 20

        # 'hot', 'povtor', 'active', 'rise'

    def test_get_odds(self, dc):
        resp = dc.get_odds()

        # summ of second half < 610
        assert type(resp['summ'][0]) is int
        assert resp['summ'][0] > 0
        assert resp['summ'][0] <= 610

        # summ of second half < 1331
        assert type(resp['summ'][1]) is int
        assert resp['summ'][1] > 0
        assert resp['summ'][1] <= 1331

        # summ of first and second halfs == total summ
        summ = resp['summ'][0] + resp['summ'][1]
        assert summ == resp['summ'][2]

        for k, v in resp.items():
            if (k != 'summ'):
                assert v[0] > 0
                assert v[0] < 81
                assert v[1] != ''
                assert v[2] != ''
