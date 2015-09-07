#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta


def date_range(first, last, days=None):
    """
        Arguments:
            first > datetime.date
            last  > datetime.date
            days  > [ int from 0 to 6 ]
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
    d_range = range(0, dlina)

    """ дублирование для скорости """
    if days:
        for x in d_range:
            day = last - timedelta(days=x + 1)
            if day.weekday() in days:
                date_list.append(day)
    else:
        for x in d_range:
            day = last - timedelta(days=x + 1)
            date_list.append(day)

    return (date_list)


if __name__ == '__main__':
    last = date.today()
    first = date(2015, 8, 1)
    week_days = [2, 5]
    dr = date_range(first, last, week_days)
    [print(dt) for dt in dr]
