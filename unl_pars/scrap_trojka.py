#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from datetime import datetime

details = {
    "action": "show_results_loto3",
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
    "Referer": "http://lottery.com.ua/ru/lottery/loto3/results.htm",
    "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, \
like Gecko) Ubuntu Chromium/40.0.2214.111 Chrome/40.0.2214.111 \
Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

last_lot3 = 3866
day_today = datetime.now().timetuple().tm_yday

details["draw"] = last_lot3 + day_today


lot3_data = requests.post(link, data=details, headers=head_dict).json()
lot3_list = [lot3_data['n' + str(ran)] for ran in [1, 2, 3]]

print('{} {}-{} {}.{}.{} {}'.format(
    lot3_data["draw"], lot3_data["lototron"], lot3_data["ballset"],
    lot3_data["day"], lot3_data["month"], lot3_data["year"], lot3_list))
