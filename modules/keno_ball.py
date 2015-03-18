#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def ball_counter(draws, tirag):
    """
    Arguments:
        draws @ list >> list >> int:
            [64,48,79,70,40, ... 13,76,72,26,65],

    Returns:
        resp_list @ list: len == 80 >> dict:
        {
            draw: 5030,
            ball: 34,
            drop: 1190,
            span 3.97,
            miss: 7,
            mrow: 6,
            mpas: 31,
            tier: [
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

        [dropped, length] = [0, 0]

        # series of inrows and passes
        [ser_inrow, ser_pass] = [[0] * 40, [0] * 40]

        # initialization of vecto
        vect = 1 if (ball in draws[0]) else -1

        # iterate ball thru draws
        for draw in draws:
            if ball in draw:
                dropped += 1
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

        missing = 0
        for draw in draws:
            if ball not in draw:
                missing += 1
            else:
                break

        period = len(draws) / dropped

        resp_list.append(dict(
            draw=tirag,
            ball=ball,
            drop=dropped,
            span=period,
            miss=missing,
            mrow=len(ser_inrow),
            mpas=len(ser_pass),
            tier=[
                pop_zeros(ser_inrow),
                pop_zeros(ser_pass)
            ]
        ))

    return resp_list
