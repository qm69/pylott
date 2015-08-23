#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $ py.test -v -s test_keno_part.py

import sys
import pytest

# http://stackoverflow.com/questions/714063/
sys.path.append('/home/qm69/code/python/lottery')

from pylott.libs.keno_tenth import part_counter
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

    @pytest.fixture(scope="module")
    def pc():  # == parts_counter
        return part_counter(draw_list, 5034)

    class TestClass:

        def test_part_counter(self, pc):

            # test the whole list
            assert type(pc) is list
            assert len(pc) == 72

            # test each ball from list
            for part in pc:

                assert type(part) is dict
                # assert len(part) == 10

                # part
                part_list = [
                    '01-10', '11-20', '21-30', '31-40',
                    '41-50', '51-60', '61-70', '71-80']
                assert part['part'] in part_list

                # bulk
                bulk_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                assert part['bulk'] in bulk_list

                # dropped
                assert part['drop'] >= 0

                # era
                assert type(part["era"]) is float
                assert len(str(part["era"]).split('.')[1]) == 1

                # mute
                assert part["mute"] >= 0

                # max era = 25, mute = 180
                if part["bulk"] == 0:
                    assert part["era"] < 29
                    assert part["mute"] < 270
                    assert part["mpas"] < 270

                # max era = 5.9, mute = 56
                elif part["bulk"] == 1:
                    assert part["era"] < 10
                    assert part["mute"] < 75
                    assert part["mpas"] < 75

                # max era = 3.6, mute = 30
                if part["bulk"] == 2:
                    assert part["era"] < 7
                    assert part["mute"] < 50
                    assert part["mpas"] < 50

                # max era = 3.9, mute = 31
                if part["bulk"] == 3:
                    assert part["era"] < 8
                    assert part["mute"] < 50
                    assert part["mpas"] < 50

                # max era = 7.6, mute 155
                if part["bulk"] == 4:
                    assert part["era"] < 10
                    assert part["mute"] < 225
                    assert part["mpas"] < 225

                # max era = 21.4, mute = 171
                if part["bulk"] == 5:
                    assert part["era"] < 30
                    assert part["mute"] < 270
                    assert part["mpas"] < 270

                # max era = 101.1, mute 438
                if part["bulk"] == 6:
                    assert part["era"] < 150
                    assert part["mute"] < 670
                    assert part["mpas"] < 670

                # max era = ???, mute > 1000
                if part["bulk"] == 7:
                    pass

                # pera
                assert type(part["pera"]) is list
                assert part["pera"][0] <= part["pera"][1]
                assert part["pera"][1] <= part["pera"][2]

                # rate
                assert type(part["rate"]) is float
                assert len(str(part["rate"]).split('.')[1]) == 1

                print(part)
