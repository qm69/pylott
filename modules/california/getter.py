#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from datetime import datetime
pref = 'http://www.calottery.com/play/draw-games/'
link_dict = dict(daily_3='daily-3', daily_4='daily-4')


def main_page(link):
    r = requests.get(link)
    if r.status_code != 200:
        raise Exception('Status code is {}'.format(r.status_code))

    resp_dict = {}
    soup = BeautifulSoup(r.content)
    soup.encode("utf8")
    soup_find = soup.find(id='content').find_all(class_='row')

    for sf in soup_find:
        draw = sf.find(class_='winning_number_sm').text.strip()
        draw_data = [int(b) for b in draw]

        rows_text = sf.find(class_='date').text.strip()
        for k in ['\xa0', '\r', '\n', '#', 'Winning Numbers', 'Draw', ',', '|', '   ', '2015']:
            rows_text = rows_text.replace(k, '')

        # ['Thursday', 'September', '17', '2015', 'Midday', '13258']
        # ['Wednesday', 'September', '16', 'Evening', '13257']
        text_list = rows_text.split(' ')
        list_len = len(text_list)

        draw_numb = int(text_list[4]) if list_len == 5 else int(text_list[5])
        date_text = '{} {} 2015'.format(text_list[1], text_list[2])
        suit_text = text_list[3] if list_len == 5 else text_list[4]

        resp_dict[draw_numb] = dict(
            firm='California',
            date=datetime.strptime(date_text, '%B %d %Y'),
            draw=draw_numb,
            rslt=draw_data,
            srtd=sorted(draw_data, key=lambda i: i),
            suit=['m'] if suit_text == 'Midday' else ['e'])

    return resp_dict


def past_page(game_name):
    link = pref + link_dict[game_name]
    r = requests.get(link + '/winning-numbers')
    if r.status_code != 200:
        raise Exception('Status code is {}'.format(r.status_code))

    resp_dict = {}
    soup = BeautifulSoup(r.content)
    soup.encode("utf8")
    soup_find = soup.find(class_='numbers').find_all('tr')[1:]

    for sf in soup_find:
        td_data = sf.find_all('td')
        temp_text = td_data[0].text.strip() + ' ' + td_data[1].text
        # Play 3 >> ['Sep', '16', '2015', '-', '13257', 'Evening', '238']
        # Play 4 >> ['Sep', '17', '2015', '-', '2678', '5948']
        text_list = temp_text.replace(',', '').split(' ')

        draw_numb = int(text_list[4])
        date_text = '{} {} {}'.format(*text_list[:3])
        draw_data = [int(b) for b in text_list[-1]]

        resp_dict[draw_numb] = dict(
            firm='California',
            date=datetime.strptime(date_text, '%b %d %Y'),
            draw=draw_numb,
            rslt=draw_data,
            srtd=sorted(draw_data, key=lambda i: i),
            suit=['m'] if text_list[5] == 'Midday' else ['e'])

    main_data = main_page(link)
    resp_keys = resp_dict.keys()
    for k, v in main_data.items():
        if k not in resp_keys:
            resp_dict[k] = v

    return resp_dict
