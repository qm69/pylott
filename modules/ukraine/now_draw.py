#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime as dt


def draw_numb(game):
    """ All Works For 2015 year """
    base = dt.date.today()
    dt_now = dt.datetime.now()
    today_weekday = dt_now.weekday()
    day_of_year = dt_now.timetuple().tm_yday

    # Кено
    if game == 'keno':
        i = 1 if dt_now.hour < 23 else 0
        # последний тираж 2014 года
        return 5013 + int(day_of_year) - i
    # Лото Трійка
    elif game == 'troika':
        i = 1 if dt_now.hour < 23 else 0
        # последний тираж 2014 года
        return 3866 + int(day_of_year) - i
    # Супер Лото
    elif game == 'maxima':
        maxima_draw, maxima_days = 949, [1, 3, 6]
        # если сегодня день тиража, но еще не наступил
        start = 1 if (today_weekday in maxima_days and
                      dt_now.hour < 23) else 0
        for x in range(start, day_of_year):
            temp = base - dt.timedelta(days=x)
            week_day = dt.datetime.weekday(temp)
            if week_day in maxima_days:
                maxima_draw += 1
        return maxima_draw
    # Супер Лото
    elif game == 'super':
        super_draw, super_days = 1433, [2, 5]
        # если сегодня день тиража, но еще не наступил
        start = 1 if (today_weekday in super_days and
                      dt_now.hour < 23) else 0
        for x in range(start, day_of_year):
            temp = base - dt.timedelta(days=x)
            week_day = dt.datetime.weekday(temp)
            if week_day in super_days:
                super_draw += 1
        return super_draw
    else:
        raise Exception('Unknown Lottery')

if __name__ == '__main__':
    print(draw_numb('keno'))
    print(draw_numb('troika'))
    print(draw_numb('maxima'))
    print(draw_numb('super'))
