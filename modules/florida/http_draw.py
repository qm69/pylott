#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from datetime import date, time, datetime
"""
hash_list = ['27-08-2015-m', '26-08-2015-n', '26-08-2015-m', '24-08-2015-m',
             '27-08-2015-n', '24-08-2015-n', '25-08-2015-m', '25-08-2015-n']
[print(l) for l in tuple(sorted(hash_list, reverse=True))]
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


def get_draw(game, dd):
    """
        smth about """
    link = linker(game, dd)
    # content, encoding, headers, json, raw, status_code, text
    r = requests.get(link)
    if r.status_code != 200:
        raise Exception('Status code is {}'.format(r.status_code))

    soup = BeautifulSoup(r.content)

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
                firm='California',
                game='Cash 3' if game == 'cash_3' else 'Play 4',
                suit=['M' if index == 0 else 'E'],
                date=datetime.combine(dd, tm),
                rslt=rslt)
            rslt_list.append(data)

        return rslt_list

    elif game == 'lucky_money':
        sf = soup.find(class_='winningNumbers')
        if not sf:
            raise Exception('There is no Resalts on the Page:\n{}'.format(link))

        td_balls = [0, 2, 4, 6, 8]
        spans = sf.find_all('span')
        data = dict(
            firm='California',
            game='Lucky Money',
            # suit=['M' if index == 0 else 'E'],
            date=datetime.combine(dd, time(hour=23, minute=15)),
            rslt=[int(s.text.strip()) for s in spans if spans.index(s) in td_balls])

        return data

if __name__ == '__main__':
    print(get_draw('cash_3', date(2015, 8, 18)))
    print(get_draw('play_4', date(2015, 8, 7)))
    print(get_draw('lucky_money', date(2015, 7, 21)))
