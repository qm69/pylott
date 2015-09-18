#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from datetime import date, time, datetime

""" Eastern Time > UTC-4 летом и UTC-5 зимой
Florida Lotto => 6 x 53 | Wednesday and Saturday @ 11:15 p.m., Eastern Time.
Powerball     => 5 x 59 + 1 x 35 | Wednesday and Saturday @ 10:59 p.m., Eastern Time.
Mega Millions => 5 x 75 + 1 x 15 | Tuesday and Friday @ 11:00 p.m., Eastern Time.
Fantasy 5     => 5 x 36 | Daily @ 11:15 p.m. Eastern Time.
Lucky Money   => 4 x 47 + 1 x 19 | Tuesday and Friday @ 11:15 p.m., Eastern Time.
Play 4        => 4 x 10 | Midday @ 1:30 p.m. and Evening @ 7:57 p.m. Eastern Time.
Cash 3        => 3 x 10 | Midday @ 1:30 p.m. and Evening @ 7:57 p.m. Eastern Time.
"""


def linker(game_name, draw_date):
    """
    Arguments:
        game: game name as 'str'
        draw_date: draw_date as 'datetime.date'
    """
    name_dict = dict(cash_3=['CASH3', 'n1In=&n2In=&n3In=&'],
                     play_4=['PLAY4', 'n1In=&n2In=&n3In=&n4In=&'],
                     lucky_money=['LUCKYMONEY', 'n1In=&n2In=&n3In=&n4In=&lbIn=&'])
    assert game_name in name_dict.keys()
    assert type(draw_date) == date

    link = ("http://www.flalottery.com/site/"
            "winningNumberSearch?"
            "searchTypeIn=date&"
            "gameNameIn={game_name}&"
            "singleDateIn={month:0>2}%2F{day:0>2}%2F{year}&"
            "fromDateIn=&toDateIn=&{ball_range}"
            "submitForm=Submit")

    link_dict = dict(game_name=name_dict[game_name][0],
                     ball_range=name_dict[game_name][1],
                     year=draw_date.year, month=draw_date.month, day=draw_date.day)

    return link.format(**link_dict)


def get_resalts(game, dd):
    """ smth about """
    link = linker(game, dd)
    # content, encoding, headers, json, raw, status_code, text
    r = requests.get(link)
    if r.status_code != 200:
        raise Exception('Status code is {}'.format(r.status_code))

    soup = BeautifulSoup(r.content)
    soup.encode("utf8")
    if game == 'cash_3' or game == 'play_4':
        sf = soup.find(class_='winningNumbersResults')
        if not sf:
            raise Exception('There is no Resalts on the Page:\n{}'.format(link))

        rslt_list = []
        td_balls = [1, 3, 5] if game == 'cash_3' else [1, 3, 5, 7]
        td_list = sf.find(class_='games').find_all('tr')[0].find_all('td')

        for index, td in tuple(enumerate(td_list)):
            spans = td.find_all('span')
            rslt = [int(s.text.strip()) for s in spans if spans.index(s) in td_balls]
            tm = time(hour=13, minute=30) if index == 0 else time(hour=19, minute=57)

            data = dict(
                firm='Florida',
                game='Cash 3' if game == 'cash_3' else 'Play 4',
                suit=['m' if index == 0 else 'e'],
                date=datetime.combine(dd, tm),
                rslt=rslt,
                srtd=sorted(rslt, key=lambda i: i))
            rslt_list.append(data)

        return rslt_list

    elif game == 'lucky_money':
        sf = soup.find(class_='winningNumbers')
        if not sf:
            raise Exception('There is no Resalts on the Page:\n{}'.format(link))

        td_balls = [0, 2, 4, 6, 8]
        spans = sf.find_all('span')
        data = dict(
            firm='Florida',
            game='Lucky Money',
            date=datetime.combine(dd, time(hour=23, minute=15)),
            rslt=[int(s.text.strip()) for s in spans if spans.index(s) in td_balls])

        return data

if __name__ == '__main__':
    print(get_resalts('cash_3', date(2015, 8, 18)))
    print(get_resalts('play_4', date(2015, 8, 7)))
    print(get_resalts('lucky_money', date(2015, 7, 21)))
