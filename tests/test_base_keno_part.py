#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $ py.test -v test_base_keno_ball.py

import sys
import pytest

# http://stackoverflow.com/questions/714063/
sys.path.append('/home/qm69/code/python/lottery')

from pylott.modules.base_keno_part import tenth_counter
from pylott.results.keno_list_1000 import draw_list

"""
@pytest.fixture(scope="module")
@pytest.fixture(scope="session")
@pytest.fixture(scope="function")
@pytest.fixture(params=["mod1", "mod2"])
"""


@pytest.fixture(scope="module")
def tc():  # == tenth_counter
    return tenth_counter(draw_list)


class TestClass:

    def test_part_counter(self, tc):

        # test the whole list
        assert type(tc) is list
        assert len(tc) == 10

        # test each ball from list
        for ten in tc:
            assert type(ten) is dict

            # tenth
            assert type(ten['tenth']) is int
            assert ten['tenth'] <= 10 and ten['tenth'] >= 0
