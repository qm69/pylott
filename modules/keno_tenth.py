#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def part_counter(draws, tirag):
    """
    Arguments:
        draws @ list >> list >> int:
        ['5018', '2015-01-05', 'B', '2', [61, 8, ... 1, 65]

    Returns:
        resp_list @ list: len == (8 * 9) == 72 >> dict:
        {
            draw: 5034,      # int
            part: '41-50',   # str
            bulk: 0,         # int
            drop: 55,        # int
            era: 18.8,       # float
            mute: 18,        # int
            pera: [0, 3, 5], # list >> int,
            rate: 0.6        # float
            mpas: 91,        # int
            pcen: ???        # int
        }
    """

    # THEN data about the periods of part
    # TAKE from the db.keno.parts
    part_bulk = {
        '01-10': {
            'first': 1, 'last': 10,
            'stats': [23.0, 5.8, 3.4, 3.7, 6.9, 18.2, 73.1, 594.2, 0]
        },
        '11-20': {
            'first': 11, 'last': 20,
            'stats': [18.9, 5.2, 3.3, 3.9, 7.6, 19.7, 101.1, 950.8, 0]
        },
        '21-30': {
            'first': 21, 'last': 30,
            'stats': [25.0, 5.7, 3.4, 3.7, 6.5, 19.4, 88.0, 528.2, 4754.0]
        },
        '31-40': {
            'first': 31, 'last': 40,
            'stats': [20.0, 5.6, 3.5, 3.7, 6.8, 19.8, 86.4, 1188.5, 0]
        },
        '41-50': {
            'first': 41, 'last': 50,
            'stats': [22.3, 5.3, 3.4, 3.8, 6.9, 20.0, 95.1, 528.2, 4754.0]
        },
        '51-60': {
            'first': 51, 'last': 60,
            'stats': [21.0, 5.8, 3.4, 3.8, 6.6, 18.1, 886.1, 679.1, 0]
        },
        '61-70': {
            'first': 61, 'last': 70,
            'stats': [24.0, 5.9, 3.6, 3.6, 6.2, 18.6, 67.9, 365.7, 0]
        },
        '71-80': {
            'first': 71, 'last': 80,
            'stats': [19.7, 5.1, 3.5, 4.0, 6.9, 21.4, 82.0, 475.0, 4754.0]
        }
    }

    counted_parts = []

    # '11-20' ... '71-80'
    for part in [p for p in part_bulk]:
        # 0 ... 8
        for amount in list(range(0, 9)):

            # series of inrows and passes
            [dropped, length, max_pass, dropped] = [0, 0, 0, 0]
            [f, l] = [part_bulk[part]['first'], part_bulk[part]['last']]

            # initialization of first vector
            vec_shtuk = len([d for d in draws[0][4] if d >= f and d <= l])
            vect = 1 if (amount == vec_shtuk) else -1

            # dropped & max_pass
            for draw in draws:
                # counts the number of balls
                shtuk = len([d for d in draw[4] if d >= f and d <= l])

                # iterate for max silent
                if amount == shtuk:

                    # summ dropped
                    dropped += 1

                    if vect < 0:
                        if max_pass < length:
                            max_pass = length
                        length = 0
                        vect = 1
                    else:
                        length += 1
                else:
                    if vect > 0:
                        length = 0
                        vect = -1
                    else:
                        length += 1

            silence = 0
            for draw in draws:
                shtuk = len([d for d in draw[4] if d >= f and d <= l])
                if shtuk != amount:
                    silence += 1
                else:
                    break

            max_pass = max_pass if (max_pass != 0) else silence
            period = round((1000 / dropped), 1) if dropped > 0 else 0.0
            ratio = round(silence / period, 1) if period > 0 else 0.0

            # mult period on 1,3,5 and then round like [21, 64, 107]
            per_arr = [round(period * p) for p in [1, 3, 5]]
            per_per = [0, 0, 0]
            for i, per in enumerate(per_arr):
                for draw in draws[:per]:
                    shtuk = len([d for d in draw[4] if d >= f and d <= l])
                    if amount == shtuk:
                        per_per[i] += 1

            counted_parts.append(dict(
                draw=tirag,
                part=part,
                bulk=amount,
                drop=dropped,
                era=period,
                mute=silence,
                pera=per_per,
                rate=ratio,
                mpas=max_pass
            ))

    return counted_parts
