#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import requests
from datetime import datetime, tzinfo, timedelta

link = "http://lottery.com.ua/index.php"
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

game_name = dict(keno='Кено', loto3='Лото Трійка', maxima='Лото Максима', sloto='Супер Лото')

""" Response{
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


def get_resalts(game, draw_num):
    resp = requests.post(
        "http://lottery.com.ua/index.php",
        headers=head_dict,
        data=dict(
            # keno, loto3, maxima, sloto
            action="show_results_" + game,
            module="lottery",
            is_ajax="true",
            draw=draw_num)).json()
    # resp = json.loads(rqst.text)
    kiev = TimeZone('Europe/Kiev', 3)
    data = dict(
        firm='УНЛ',  # 'УНЛ'
        draw=draw_num,
        game=game_name[game],
        suit=[resp["lototron"], resp["ballset"]],
        # BSON -> tzinfo save with
        date=datetime(resp["year"], resp["month"], resp["day"], 23, 0, 0, 0))

    regex, items = re.compile('[n]\d+'), resp.items()
    draw_list = sorted([[k[1:], v] for k, v in items if regex.findall(k)], key=lambda k: k[0])
    rslt = [r[1] for r in draw_list]
    data['rslt'] = rslt
    data['srtd'] = sorted(rslt, key=lambda i: i)

    return data

if __name__ == '__main__':
    print(get_resalts('maxima', 1050))
    print(get_resalts('sloto', 1500))
    print(get_resalts('loto3', 4098))
    print(get_resalts('keno', 5248))
