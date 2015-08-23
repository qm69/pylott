#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from termcolor import colored
# print(colored('hello', 'red'), colored('world', 'green'))


def counter(total, value):
    return colored('0' + str(value) if value < 10 else value,
                   'red' if value < total else 'magenta')


def one(total, value):
    return colored(value, 'magenta' if (value > total) else
                   'red' if (value < total) else 'yellow')


def odd(arg):
    return colored('odds', 'magenta') if arg else colored('even', 'red')


def more(arg):
    return colored('more', 'magenta') if arg else colored('less', 'red')


def amount(draw, form, to):
    # [], [7], [7, 8], [7, 8, 9]
    data = list(filter(lambda el: el >= form and el <= to, draw))
    arry = ['blue', 'green', 'yellow', 'white']
    data_len = len(data)
    return colored(data_len, arry[data_len])


def summ(draw, form, to, total):
    """ diapazon Summ """
    filt = sorted(draw, key=lambda el: el >= form and el <= to)
    summ = sum(filt) if len(filt) > 0 else 0
    return colored('0' + str(summ) if summ < 10 else summ,
                   'red' if summ < total else 'magenta')


if __name__ == '__main__':
    draw = [7, 8, 9]
    # counter
    print(counter(4.5, 12), counter(4.5, 6))
    # one
    print(one(5, 4), one(3, 4), one(4, 4))
    # odd
    print(odd(True), odd(False))
    # more
    print(more(True), more(False))
    # amount
    print(amount(draw, 0, 4), amount(draw, 0, 7),
          amount(draw, 5, 8), amount(draw, 5, 9))
    # summ
    print(summ(draw, 0, 4, 15), summ(draw, 0, 7, 15),
          summ(draw, 5, 8, 30), summ(draw, 5, 9, 45))
