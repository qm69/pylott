#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $ py.test -v test_keno_ball.py

import sys
import pytest

# http://stackoverflow.com/questions/714063/
sys.path.append('/home/qm69/code/python/lottery')

from pylott.modules.keno_ball import ball_counter
from pylott.results.keno_list_1000 import draw_list


@pytest.fixture(scope="module")
def bc():  # ball_counter == bc
    return ball_counter(draw_list, 5053)


class TestClass:

    def test_ball_counter(self, bc):

        # test the whole list
        assert type(bc) is list
        assert len(bc) == 80

        # test each ball from list
        for ball in bc:
            assert type(ball) is dict
            assert len(ball) == 8

            # ball
            assert type(ball['ball']) is int
            assert ball['ball'] < 81

            # drop
            assert type(ball['drop']) is int
            assert ball['drop'] > 0

            # period
            assert type(ball['span']) is float
            assert ball['span'] < 5 and ball['span'] > 3

            # miss
            assert type(ball['miss']) is int
            assert ball['miss'] >= 0

            # max_inrow
            assert type(ball['mrow']) is int
            assert ball['mrow'] >= 0

            # max_pass
            assert type(ball['mpas']) is int
            assert ball['mpas'] >= 0

            # series
            assert type(ball['tier']) is list
            assert len(ball['tier']) == 2

            # test for zeros at the end of each list
            assert ball['tier'][0][-1] != 0
            assert ball['tier'][0][-1] != 0
