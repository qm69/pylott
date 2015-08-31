#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import time, datetime, tzinfo, timedelta

""" Eastern Time > UTC-4 летом и UTC-5 зимой
Florida Lotto => 6 x 53 | Wednesday and Saturday @ 11:15 p.m., Eastern Time.
Powerball     => 5 x 59 + 1 x 35 | Wednesday and Saturday @ 10:59 p.m., Eastern Time.
Mega Millions => 5 x 75 + 1 x 15 | Tuesday and Friday @ 11:00 p.m., Eastern Time.
Fantasy 5     => 5 x 36 | Daily @ 11:15 p.m. Eastern Time.
Lucky Money   => 4 x 47 + 1 x 19 | Tuesday and Friday @ 11:15 p.m., Eastern Time.
Play 4        => 4 x 10 | Midday @ 1:30 p.m. and Evening @ 7:57 p.m. Eastern Time.
Cash 3        => 3 x 10 | Midday @ 1:30 p.m. and Evening @ 7:57 p.m. Eastern Time.
"""


class TimeZone(tzinfo):
    def __init__(self, name, off_set):

        self.name = name
        self.offset = off_set
        self.isdst = False

    def tzname(self, dt):
        return self.name

    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)

    def dst(self, dt):
        return timedelta(hours=1) if self.isdst else timedelta(0)


def last_date(game):
    """ 'year', 'day', 'weekday', 'month', 'hour', 'minute', 'second', 'microsecond',
        'today', 'now', 'date', 'time'
        'astimezone', 'combine', 'ctime', 'fromordinal',
        'isocalendar', 'isoformat', 'isoweekday', 'max',  'min', 'fromtimestamp',
        'replace', 'resolution', 'strftime', 'strptime',
        'timestamp', 'timetuple',  'toordinal',
        'timetz', 'tzinfo', 'dst', 'tzname'
        'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple'
        """
    # florida = TimeZone('US/Florida', -4.00)
    florida_now = datetime.now()
    # print(florida_now.strftime('%m/%d/%Y %H:%M:%S %Z %z'))
    """ tm_year=2015, tm_mon=8, tm_mday=29,
        tm_hour=7, tm_min=9, tm_sec=25,
        tm_wday=5, tm_yday=241, tm_isdst=0 """
    date_tupl = florida_now.timetuple()
    year, day, month, weekday = (date_tupl[0], date_tupl[1],
                                 date_tupl[2], date_tupl[6])
    if game == 'cash_3' or game == 'play_4':
        """ возвращает datetime последнего тиража """
        cash3_draw_time = datetime(year, day, month, 13, 30, 0, 0)
        if florida_now > cash3_draw_time:
            return florida_now
        else:
            return (florida_now - timedelta(days=1))

    elif game == 'lucky_money':
        # Tuesday and Friday @ 23:15
        if weekday in [1, 4] and florida_now.time() > time(23, 15, 0):
            return florida_now
        else:
            minus_day = (1 if weekday in [2, 5] else
                         2 if weekday in [3, 6] else
                         3 if weekday in [0, 4] else 4)
            return (florida_now - timedelta(days=minus_day))
    else:
        raise Exception('No such game like: {}'.format(game))

if __name__ == '__main__':
    print(last_date('play_4'))
    print(last_date('lucky_money'))
