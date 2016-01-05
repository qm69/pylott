#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from datetime import datetime, date, timedelta
"""
Response {
    "numbersRequested": [],
    "jsonSearch": "NOT",
    "jsonMax": 1,
    "draw":[
        {"date":"09/19/2015 Midday","numbersDrawn":"5-7-3-3","luckySumDrawn":18},
        ... ,
        {"date":"09/18/2015 Midday","numbersDrawn":"2-9-9-7","luckySumDrawn":27},
    ]}
"""


class NewYork(object):
    """docstring for NewYork"""

    def __init__(self, game_name, month_first, year_first, month_last, year_last):
        self.draw_list = []
        link_dict = dict(numbers='number', win_4='win4')
        """ в каком формате получает ? """
        json_link = (
            'http://nylottery.ny.gov/wps/PA_NYSLNumberCruncher/NumbersServlet?' +
            'game={0}&' +
            'action=winningnumbers&' +
            'startSearchDate={1}/{2}&' +
            'endSearchDate={3}/{4}&' +
            'pageNo=1&' +
            'last=0&' +
            'perPage=50&' +
            'sort=0')

        link = json_link.format(link_dict[game_name], month_first, year_first, month_last, year_last)
        self.r = requests.get(link)
        if self.r.status_code != 200:
            raise Exception('Status code is {}'.format(self.r.status_code))

        for draw in self.r.json()['draw']:
            temp_date = draw['date'].split(' ')
            # ??? почему tuple
            draw_suit = 'm' if temp_date[1] == 'Midday' else 'e'
            draw_date = datetime.strptime(temp_date[0], '%m/%d/%Y')
            draw_time = timedelta(hours=15, minutes=35) if draw_suit == 'm' else timedelta(hours=20, minutes=25)
            draw_date += draw_time
            draw_rslt = [int(ball) for ball in draw['numbersDrawn'].split('-')]
            draw_dict = dict(
                date=draw_date,
                suit=[draw_suit],
                rslt=draw_rslt,
                srtd=sorted(draw_rslt, key=lambda i: i),
                firm='New York')
            self.draw_list.append(draw_dict)
        # print(self.draw_list)

    def temp_date(self):
        """ smth about method """
        return self.draw_list

    def find(self, draw_date, draw_suit):
        """ smth about method """
        for draw in self.draw_list:
            if draw_date == draw['date'].date() and draw_suit == draw['suit'][0]:
                return draw
        return None

if __name__ == '__main__':
    """ ny.draw_list: список от начала года
    {'firm': 'New York', 'rslt': [1, 5, 0, 2], 'suit': ['e'], 'srtd': [0, 1, 2, 5], 'date': datetime.datetime(2015, 11, 1, 0, 0)}
    {'firm': 'New York', 'rslt': [6, 0, 5, 2], 'suit': ['m'], 'srtd': [0, 2, 5, 6], 'date': datetime.datetime(2015, 11, 1, 0, 0)}
    """
    ny = NewYork('win_4', '12', '2015', '2', '2016')
    # print(len(ny.draw_list))
    for n in ny.draw_list:
        print(n)
    temp = ny.find(date(2015, 11, 21), 'm')
    print(temp)
