#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $ py.test -v test_base_keno_ball.py

import sys
import pytest

# http://stackoverflow.com/questions/714063/
sys.path.append('/home/qm69/code/python/lottery')

from pylott.modules.base_keno_ball import DrawCount
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
