#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $ py.test -v test_base_keno_ball.py

import sys
import pytest

# http://stackoverflow.com/questions/714063/
sys.path.append('/home/qm69/code/python/lottery')

from pylott.modules.base_keno_part import part_counter
from pylott.results.keno_list_1000 import draw_list

"""
@pytest.fixture(scope="module")
@pytest.fixture(scope="session")
@pytest.fixture(scope="function")
@pytest.fixture(params=["mod1", "mod2"])
"""


@pytest.fixture(scope="module")
def pc():  # == parts_counter
    return part_counter(draw_list)


class Tespclass:
    """
    resp_list @ list: len == (8 * 9) == 72 >> dict:
    {
      # comp: 'unl',
      # draw: 5432,
        part: '1-10',
        yield: 3, # [1 .. 9]
        drop: 420,
        percent: 30,
        period: 3.3,
        per_per: [1, 2, 2],
        max_pass: 33,
        silent: 0,
        ratio: 2.6,
        # of passing
        series: [ ... ]
    }
    """
    def test_part_counter(self, pc):

        # test the whole list
        assert type(pc) is list
        assert len(pc) == 72

        # test each ball from list
        for part in pc:
            
            assert type(part) is dict
            assert len(part) != 0

            # parts
            assert type(ten['tenth']) is int
            assert ten['tenth'] <= 10 and ten['tenth'] >= 0
