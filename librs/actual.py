#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
from datetime import time
from datetime import datetime
from datetime import tzinfo
from datetime import timedelta


class TimeZone(tzinfo):
    def __init__(self, name, off_set, is_dst):

        self.name = name
        self.offset = off_set
        self.isdst = is_dst

    def tzname(self, dt):
        return self.name

    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)

    # http://www.timeanddate.com/time/zones/est
    def dst(self, dt):
        return timedelta(hours=1) if self.isdst else timedelta(0)


def draw_date(tz_name, tz_gmt, tz_dst, draw_time, draw_day=[0, 1, 2, 3, 4, 5, 6]):
    """ Возвращает актуальную дату последнего тиража на сейчас

    print(time_zone_now.strftime('%Y/%m/%d %H:%M:%S %A %Z %z'))
    !!! Коректирвать в учную результаты тестов

    Args:
        tz_name   >> string: Название поясного времени
        tz_gmt    >> float: +/- GMT часов
        tz_dst    >> bool: Day saving time
        draw_time >> [ datetime.date ]: время розыгрыша лотереи
            [time(20, 30)] or [time(19, 57), time(19, 57)]
        draw_day  >> [ integer ]: Дни недели от 0 ... 6

    Returns:
        return datetime.date or [datetime.date, 'e' || 'm']

    >>> draw_date('EU/Belgium', 2.00, True, [time(19, 57), time(20, 30)])
    [datetime.date(2015, 9, 14), 'e']

    >>> draw_date('EU/Belgium', 2.00, True, [time(20, 30)], [3, 6])
    datetime.date(2015, 9, 13)

    >>> draw_date('EasternTime', -4.00, True, [time(19, 57), time(19, 57)], [2, 6])
    [datetime.date(2015, 9, 13), 'e']

    """
    tz_data = TimeZone(tz_name, tz_gmt, tz_dst)
    dt_now = datetime.now(tz_data)

    week_now = dt_now.weekday()
    date_now = dt_now.date()
    time_now = dt_now.time()

    if week_now in draw_day:
        # два тиража в день
        if len(draw_time) == 2:
            # сегодня и вечерний тираж состоялся
            if time_now > draw_time[1]:
                return [date_now, 'e']
            # сегодня и дневной тираж состоялся
            elif time_now > draw_time[0]:
                return [date_now, 'm']
            # сегодня, но тираж ещо не состоялся
            else:
                return [date_now - timedelta(days=1), 'e']
        else:
            # сегодня и тираж состоялся
            if time_now > draw_time[0]:
                return date_now
            # сегодня, но тираж ещо не состоялся
            else:
                return date_now - timedelta(days=1)
    else:
        # 3 in [0, 2, 4, 6] 2 << 3
        if week_now > draw_day[0]:
            last = sorted(filter(lambda x: x < week_now, draw_day), reverse=True)[0]
            resp = date_now - timedelta(days=week_now - last)
            return resp if len(draw_time) == 1 else [resp, 'e']
        # 2 in [3, 6] >> 6 << 2
        else:
            last = sorted(draw_day, reverse=True)[0]
            resp = date_now - timedelta(days=7 - (last - week_now))
            return resp if len(draw_time) == 1 else [resp, 'e']


def draw_numb(tz_name, tz_gmt, tz_dst, draw_time, last_2014, draw_day=[0, 1, 2, 3, 4, 5, 6]):
    """ Возвращает актуальный номер последнего тиража на сейчас

    Args:
        tz_name   >> string: Название поясного времени
        tz_gmt    >> float: +/- GMT часов
        tz_dst    >> bool: Day saving time
        draw_time >> [ datetime.date ]: время розыгрыша лотереи
            [time(20, 30)] or [time(19, 57), time(19, 57)]
        last_2014 >> int: последний тираж на 31 декабря 2014
        draw_day  >> [ int ]: Дни недели от 0 ... 6

    Returns:
        int

    ### Test is up to 12-09-2015
    ### $ py.test --doctest-modules -v actual.py

    # Keno
    >>> draw_numb('EU/Kiev', 2.00, True, [time(23, 0, 0)], 5013)
    5270

    # troika
    >>> draw_numb('EU/Kiev', 2.00, True, [time(23, 0, 0)], 3866)
    4123

    # Maxima
    >>> draw_numb('EU/Kiev', 2.00, True, [time(23, 0, 0)], 949, [1, 3, 6])
    1059

    # Super Loto
    >>> draw_numb('EU/Kiev', 2.00, True, [time(23, 0, 0)], 1434, [2, 5])
    1506

    # Calottery Daily 3
    >>> draw_numb('EU/Kiev', -7.00, True, [time(13, 0), time(18, 30)], 12739)
    13253
    """
    tz_data = TimeZone(tz_name, tz_gmt, tz_dst)
    dt_now = datetime.now(tz_data)

    # порядковый номер дня года ~ 213й
    days_now = dt_now.timetuple().tm_yday
    time_now = dt_now.time()
    # date_now = dt_now.date()
    # week_now = dt_now.weekday()

    resp_draw_numb = last_2014
    first_day = date(2015, 1, 1)
    # если давжды в день тогда += 2, вместо += 1
    add_numb = 2 if len(draw_time) == 2 else 1

    for day in range(0, days_now):
        temp_day = first_day + timedelta(days=day)
        week_day = datetime.weekday(temp_day)
        if week_day in draw_day:
            resp_draw_numb += add_numb

    if len(draw_time) == 2:
        # вечерний, дневной или вчерашний тираж
        minus = 0 if time_now > draw_time[1] else 1 if time_now > draw_time[0] else 2
        return resp_draw_numb - minus
    else:
        # сегоднешний или вчерашений
        minus = 0 if time_now > draw_time[0] else 1
        return resp_draw_numb - minus
