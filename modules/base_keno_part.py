#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def part_counter(draws, tirag):
    """
    Arguments:
        draws @ list >> list >> int:
            [64,48,79,70,40, ... 13,76,72,26,65],

    Returns:
        resp_list @ list: len == (8 * 9) == 72 >> dict:
        {
            part: '1-10',
            bulk: 3,    # [1 .. 9]
            drop: 420,
            pcen: 30.1, # percent
            era: 3.3,   # period
            pera: [
                1,      # drop per 1 per
                2,      # drop per 3 per
                2       # drop per 5 per
            ],          # per_pera
            mpas: 33,   # max_pass
            mute: 0,    # silent
            rate: 2.6,  # ratio
        }
    """
    counted_parts = []

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

    # internal funcion
    def part_creater(part, amount):
        return dict(
            part=part,
            bulk=amount,
            drop=0,
            pcen=0.0,
            era=0.0,
            pera=[1, 2, 2],
            mpas=0,
            mute=0,
            rate=0.0
        )

    # '11-20' ... '71-80'
    for part in [p for p in part_bulk]:
        # 0 ... 8
        for amount in list(range(0, 9)):

            asdf = part_creater(part, amount)

            # dropped & max_pass
            for draw in draws:
                f = part_bulk[part]['first']
                l = part_bulk[part]['last']
                shtuk = len([d for d in draw if d >= f and d <= l])

                # summ dropped
                if amount == shtuk:
                    asdf['drop'] += 1

                # last silent
                while (shtuk != amount):
                    asdf['silent'] += 1

                # max_pass
                [max_pass, ser_len] = [0, 0]
                vector = 1 if (shtuk == amount) else -1

                if shtuk == amount:
                    if vector < 0:
                        if ser_len > max_pass:
                            max_pass = ser_len
                        ser_len = 0
                        vector = 1
                    else:
                        ser_len += 1
                else:
                    if vector > 0:
                        ser_len = 0
                        vector = -1
                    else:
                        ser_len += 1

            """ get data of period and insert it in

            # per_per
            per_arr = [
                asdf['period'],
                asdf['period'] * 3,
                asdf['period'] * 5
            ]
            for i, perddd in enumerate(per_arr):
                for draw in draws:
                    len([d for d in draw if d >= part[1] and d <= part[2]])
                    if amount == shtuk:
                        asdf['per_per'][i-1] += 1
            """

            # count percent, period, ratio
            asdf['percent'] = asdf['drop'] / tirag  # и округлить до 2й цифры
            asdf['period'] = tirag / asdf['drop']  # и округлить до 2й цифры
            asdf['ratio'] = asdf['silent'] / asdf['period']  # окр до 2й цифры

            counted_parts.append(asdf)

    return counted_parts
