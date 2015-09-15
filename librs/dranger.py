#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date, timedelta


def drange(first, last, days=[0, 1, 2, 3, 4, 5, 6]):
    """ Smth about this function

    Arguments:
        first >> datetime.date
        last  >> datetime.date
        days  >> [ int 0 ... 6 ]

    Returns:
        [ datetime.date ]

    """
    tmpl = "{} must be a 'datetime.datetime' not a {}"
    if type(first) is not date:
        raise TypeError(tmpl.format('First', type(first)))
    if type(last) is not date:
        raise TypeError(tmpl.format('Last', type(last)))
    if days:
        if False in [wk < 7 for wk in days]:
            text = 'Weekday list contains integers more than 6'
            raise TypeError(text)

    date_list = []
    dlina = (last - first).days

    for dr in range(0, dlina):
        day = first + timedelta(days=dr + 1)
        if day.weekday() in days:
            date_list.append(day)

    return (date_list)

if __name__ == '__main__':
    last = date.today()
    first = date(2015, 7, 1)
    week_days = [0, 2, 5]
    [print(dt) for dt in drange(first, last, week_days)]
