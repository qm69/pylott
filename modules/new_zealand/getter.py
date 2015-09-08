#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import datetime as dt


def get_resalts(game, draw_numb):
    """
    https://mylotto.co.nz/index.php/play3/results/?draw=87
    """
    link_dict = dict(play_3=['play3', 'Play 3'])
    link = 'https://mylotto.co.nz/index.php/{}/results/?draw={}'\
           .format(link_dict[game][0], draw_numb)

    r = requests.get(link)
    if r.status_code != 200:
        raise Exception('Status code is {}'.format(r.status_code))

    soup = BeautifulSoup(r.content)
    soup.encode("utf8")

    if game == 'play_3':
        """
        document.getElementsByClassName('resultsTableInnerTable')[0]
                .getElementsByTagName('td')[5]
                .textContent
        """
        # уникальный - только один на странице, поетому не find_all
        sf = soup.find(class_='resultsTableInnerTable')
        if not sf:
            raise Exception('There is no Resalts on the Page:\n{}'.format(link))

        td_list = sf.find_all('td')[5]
        rslt = [int(ball) for ball in td_list.text]
        # только до 2015 года
        draw_date = dt.datetime(2015, 1, 1, 8, 30) + dt.timedelta(draw_numb - 88)

        data = dict(
            firm='New Zealand',
            game='Play 3',
            draw=draw_numb,
            date=draw_date,
            rslt=rslt,
            srtd=sorted(rslt, key=lambda i: i))

        return data

    else:
        raise Exception('Unknown Lottery')


if __name__ == '__main__':
    print(get_resalts('play_3', 299))
