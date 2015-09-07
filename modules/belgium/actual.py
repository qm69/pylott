#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date, time, datetime, tzinfo, timedelta

""" Только тиражовые оттереи
http://www.nationale-loterij.be/nl/
I. - JSON, II. - by Date
Joker +     -> 6 x 10 + 1 x 12 (1 знак зодиака)
               пн., ср., чт. и сб. > 19:00; вт и пн. > 20:00 и в вс. до 13:00.
Keno        -> 20 x 70 | after 23:00 everyday
Pick 3      -> 3 x 10  | Everyday кроме Вс. в 20:30 по GMT +2:00
Lotto       -> 6 x 45 + 1 x 45 | среда и суббота @ ~20:00.
Super Lotto -> 6 x 45? + 1
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


def draw_date(game):
    """ 'year', 'day', 'weekday', 'month', 'hour', 'minute', 'second', 'microsecond',
        'today', 'now', 'date', 'time'
        'astimezone', 'combine', 'ctime', 'fromordinal',
        'isocalendar', 'isoformat', 'isoweekday', 'max',  'min', 'fromtimestamp',
        'replace', 'resolution', 'strftime', 'strptime',
        'timestamp', 'timetuple',  'toordinal',
        'timetz', 'tzinfo', 'dst', 'tzname'
        'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple'
        """
    belgium = TimeZone('Europa/Be', +2.00)
    belgium_now = datetime.now(belgium)
    # print(belgium_now.strftime('%m/%d/%Y %H:%M:%S %Z %z'))
    """ tm_year=2015, tm_mon=8, tm_mday=29,
        tm_hour=7, tm_min=9, tm_sec=25,
        tm_wday=5, tm_yday=241, tm_isdst=0
    """
    date_tupl = belgium_now.timetuple()
    year, month, day = date_tupl[0:3]
    weekday = date_tupl[6]
    if game == 'pick_3' or game == 'keno':
        # Ежедневно кроме Вс. в ~20:30 по GMT+2:00
        resp_date = date(year, month, day)
        if weekday != 6 and belgium_now.time() > time(20, 30, 0):
            return resp_date
        else:
            return resp_date - timedelta(days=1)
    else:
        raise Exception('No such game like: {}'.format(game))

if __name__ == '__main__':
    print(draw_date('pick_3'))
