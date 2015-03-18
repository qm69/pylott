#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

details = {
    "draw": "5084",
    "action": "show_results_keno",
    "module": "lottery",
    "is_ajax": "true",
}
link = "http://lottery.com.ua/index.php"
head_dict = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru,en-US;q=0.8,en;q=0.6,uk;q=0.4",
    "Connection": "keep-alive",
    "Content-Length": "62",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "lottery.com.ua",
    "Origin": "http://lottery.com.ua",

    "Referer": "http://lottery.com.ua/ru/lottery/keno/results.htm",

    "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, \
like Gecko) Ubuntu Chromium/40.0.2214.111 Chrome/40.0.2214.111 \
Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

r = requests.post(link, data=details, headers=head_dict)

rd = r.json()
del rd["result"]

res_arr = [rd['n' + str(ran)] for ran in list(range(1, 21))]
print(rd["draw"], res_arr)
print(rd["lototron"], rd["ballset"], rd["day"], rd["month"], rd["year"])
