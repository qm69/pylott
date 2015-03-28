#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $ py.test -v -s test_keno_part.py

import sys
import pytest

# http://stackoverflow.com/questions/714063/
sys.path.append('/home/qm69/code/python/lottery')

from pylott.modules.unl_getter import get_keno


@pytest.fixture(scope="module")
def gk():  # == parts_counter
    return get_keno(5034)


class TestClass:

    def test_get_keno(self, gk):

        assert type(gk) is dict

        assert gk["draw"] is not None
        assert type(gk["draw"]) is int

        assert gk["n1"] is not None
        assert gk["n20"] is not None

        balls = [str(gk['n' + str(r)]) for r in list(range(1, 21))]
        assert len(balls) == 20
