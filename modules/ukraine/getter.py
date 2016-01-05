#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import requests
from datetime import datetime

user_agent = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko)\
              Ubuntu Chromium/40.0.2214.111 Chrome/40.0.2214.111 Safari/537.36"
head_dict = {"Accept": "application/json, text/javascript, */*; q=0.01",
             "Accept-Encoding": "gzip, deflate",
             "Accept-Language": "ru,en-US;q=0.8,en;q=0.6,uk;q=0.4",
             "Connection": "keep-alive",
             "Content-Length": "62",
             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
             "Host": "lottery.com.ua",
             "Origin": "http://lottery.com.ua",
             "User-Agent": user_agent,
             "X-Requested-With": "XMLHttpRequest"}

game_name = dict(keno='Кено',
                 loto3='Лото Трійка',
                 maxima='Лото Максима',
                 sloto='Супер Лото')

""" Response {
    "result":"\t\t\t\t\t\t\t\t\t\t\t<div class=\"tab_val_line\">\n\t\t\t\t\t\t\t\t\t\t\t\t<div class=\"tab_val_item
     money\">500.<span>00<\/span><\/div>\n\t\t\t\t\t\t\t\t\t\t\t\t<div class=\"tab_val_item\">8<\/div>\n
    \t\t\t\t\t\t\t\t\t\t\t\t<div class=\"tab_val_item\">\u0422\u043e\u0447\u043d\u0438\u0439 \u0432\u0438
    \u0433\u0440\u0430\u0448<\/div>\n\t\t\t\t\t\t\t\t\t\t\t<\/div>\n\t\t\t\t\t\t\t\t\t\t\t<div class=\"tab_val_line
    \">\n\t\t\t\t\t\t\t\t\t\t\t\t<div class=\"tab_val_item money\">160.<span>00<\/span><\/div>\n\t\t\t\t
    \t\t\t\t\t\t\t\t<div class=\"tab_val_item\">10<\/div>\n\t\t\t\t\t\t\t\t\t\t\t\t<div class=\"tab_val_item
    \">\u0414\u043e\u0432\u0456\u043b\u044c\u043d\u0438\u0439<\/div> \n\t\t\t\t\t\t\t\t\t\t\t<\/div> \n\t
    \t\t\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t\t\t\t\t",
    "all_humans":"18 <span>\u0448\u0442\u0443\u043a<\/span>",
    "all_prize":"5 600",
    "day_name":"\u0427\u0435\u0442\u0432\u0435\u0440",
    "month_name":"\u0421\u0435\u0440\u043f\u0435\u043d\u044c",
    "amonth_name":"\u0421\u0435\u0440\u043f\u043d\u044f",
    "year":2015, "month":8, "day":20,
    "draw":"4098", "ndraw":4099, "pdraw":4097,
    "n1":7, "n2":7, "n3":6,
    "lototron":"\u0410",
    "ballset":"2",
}"""


def get_resalts(game, draw_num):
    resp = requests.post(
        "http://lottery.com.ua/index.php",
        headers=head_dict,
        data=dict(
            action="show_results_" + game,  # keno, loto3, maxima, sloto
            module="lottery",
            is_ajax="true",
            draw=draw_num)
    ).json()
    data = dict(
        firm='УНЛ',  # 'УНЛ'
        draw=draw_num,
        game=game_name[game],
        suit=[resp["lototron"], resp["ballset"]],
        date=datetime(resp["year"], resp["month"], resp["day"], 20, 0))

    regex = re.compile('[n]\d+')
    items = resp.items()
    """ ('n3', 18), ('n15', 27) ... ('n12', 57), ('n7', 57) """
    unsrtd = [(int(k[1:]), v) for k, v in items if regex.findall(k)]
    """ ('n1', 66), ('n2', 54) ... ('n19', 57), ('n20', 57) """
    srtd = sorted(unsrtd, key=lambda k: k[0])
    draw_list = [second for first, second in srtd]

    data['rslt'] = draw_list
    data['srtd'] = sorted(draw_list, key=lambda i: i)

    return data

if __name__ == '__main__':
    print(get_resalts('maxima', 1050))
    print(get_resalts('sloto', 1500))
    print(get_resalts('loto3', 4232))
    print(get_resalts('keno', 5333))
