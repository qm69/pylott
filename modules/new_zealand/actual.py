#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime as dt


def draw_numb(game):
    """ All Works For 2015 year """
    dt_now = dt.datetime.now()
    day_of_year = dt_now.timetuple().tm_yday
    draw_time = dt.time(hour=8, minute=30)

    if game == 'play_3':
        i = 1 if dt_now.time() < draw_time else 0
        # 31 декабря 2014 тираж №87
        return 87 + int(day_of_year) - i
    else:
        raise Exception('Unknown Lottery')

if __name__ == '__main__':
    print(draw_numb('play_3'))
