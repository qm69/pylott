#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $ py.test -v test_base_keno_ball.py

import sys
import pytest

# http://stackoverflow.com/questions/714063/
sys.path.append('/home/qm69/code/python/lottery')

from pylott.modules.base_keno_ball import ball_counter
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
def bc():  # ball_counter == bc
    return ball_counter(draw_list)


class TestClass:

    @classmethod
    def setup_class(cls):
        pass

    def test_ball_counter(self, bc):

        # test the whole list
        assert type(bc) is list
        assert len(bc) == 80

        # test each ball from list
        for ball in bc:
            assert type(ball) is dict

            assert type(ball['ball']) is int
            assert ball['ball'] < 81

            assert type(ball['dropped']) is int
            assert ball['dropped'] > 0

            assert type(ball['period']) is float
            assert ball['period'] < 5
            assert ball['period'] > 3

            assert type(ball['missed']) is int
            assert ball['missed'] >= 0

            assert type(ball['silent']) is int
            assert ball['silent'] >= 0

            assert type(ball['max_pass']) is int
            assert ball['max_pass'] >= 0

            assert type(ball['max_inrow']) is int
            assert ball['max_inrow'] >= 0

            assert type(ball['series']) is list
            assert len(ball['series']) == 2
