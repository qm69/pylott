#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def ball_counter(draws):
    """
    Arguments:
        draws @ list >> list >> int:
            [64,48,79,70,40, ... 13,76,72,26,65],

    Returns:
        resp_list @ list: len == 80 >> dict:
        {
            'ball': 34,
            'drop': 1190,
            'period': 3.97,
            'miss': 1,
            'silent': 12,
            'max_pass': 28,
            'max_inrow': 9,
            series: [
                [347, 123, 67, 45, 23, 12, 6, 3, 1],
                [443, 117, 69, 51, 31, 15, 9, 6, 3, 1],
            ]
        }
    """
    resp_list = []

    def pop_zeros(items):
        """
        incapsulated internal fuction that
        trim zeros in 'ser_inrow' & 'ser_pass'
        """
        while items[-1] == 0:
            items.pop()
        return items

    for ball in list(range(1, 81)):

        # выпадения и длина серии
        [drop, length] = [0, 0]

        # серия выпадения и серия пропуска
        [ser_inrow, ser_pass] = [[0] * 40, [0] * 40]

        # первое направления вектора для серии
        vect = 1 if (ball in draws[0]) else -1

        # iterate ball thru draws
        for draw in draws:
            if ball in draw:
                drop += 1
                if vect < 0:
                    ser_pass[length] += 1
                    length = 0
                    vect = 1
                else:
                    length += 1
            else:
                if vect > 0:
                    ser_inrow[length] += 1
                    length = 0
                    vect = -1
                else:
                    length += 1
        period = len(draws) / drop

        resp_list.append(dict(
            ball=ball,
            drop=drop,
            period=period,
            miss=0,
            silent=0,
            max_inrow=len(ser_inrow),
            max_pass=len(ser_pass),
            series=[
                pop_zeros(ser_inrow),
                pop_zeros(ser_pass)
            ]
        ))

    return resp_list
