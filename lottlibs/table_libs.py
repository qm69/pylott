#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from termcolor import colored


def true_false(arg1, arg2, value):
    return colored(arg1 if value else arg2, 'magenta' if value else 'red')


def summ_amnt(draw, form, to, total=None):
    data = list(filter(lambda el: el >= form and el <= to, draw))
    if total:
        suma = sum(data)
        return colored('0' + str(suma) if suma < 10 else suma,
                       'red' if suma < total else 'magenta')
    else:
        colors = ['blue', 'green', 'yellow', 'white', 'white']
        data_len = len(data)
        return colored(data_len, colors[data_len])


def counter(value, total, zero=None):
    if zero:
        return colored('0' + str(value) if value < 10 else value,
                       'red' if value < total else 'magenta')
    else:
        return colored(value, 'magenta' if (value > total) else
                              'red' if (value < total) else 'yellow')
