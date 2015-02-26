#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def ball_counter(draws):
    """
    Arguments:

        draws @ list >> list >> int; like:
        [...
            [64,48,79,70,40,69,20,59,66,61,80,53,78,57,28,13,76,72,26,65],
        ...]

    Returns:

        @ list >> dict;
        [... {
            'ball': 34,

            'dropped': 1190,
            'period': 3.97,

            'missed': 1,
            'silent': 12,

            'max_pass': 28,
            'max_inrow': 9,

            series: [
                [347, 123, 67, 45, 23, 12, 6, 3, 1],
                [443, 117, 69, 51, 31, 15, 9, 6, 3, 1],
            ]
        }, ...]
    """
    response = []
    for num in list(range(1, 81)):
        for draw in draws:
            pass

    return []
