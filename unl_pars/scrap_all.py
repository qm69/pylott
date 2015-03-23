#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from datetime import datetime

user_agent = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) \
              Ubuntu Chromium/40.0.2214.111 Chrome/40.0.2214.111 Safari/537.36"
head_dict = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru,en-US;q=0.8,en;q=0.6,uk;q=0.4",
    "Connection": "keep-alive", "Content-Length": "62",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "lottery.com.ua",
    "Origin": "http://lottery.com.ua",
    "User-Agent": user_agent,
    "X-Requested-With": "XMLHttpRequest"
}
link = "http://lottery.com.ua/index.php"

dict_keno = dict(action="show_results_keno", module="lottery", is_ajax="true")
dict_lot3 = dict(action="show_results_loto3", module="lottery", is_ajax="true")

[last_lot3, last_keno] = [3866, 5013]
day_today = datetime.now().timetuple().tm_yday

dict_keno["draw"] = day_today + last_keno
dict_lot3["draw"] = day_today + last_lot3

keno_data = requests.post(link, data=dict_keno, headers=head_dict).json()
keno_list = [keno_data['n' + str(ran)] for ran in list(range(1, 21))]

lot3_data = requests.post(link, data=dict_lot3, headers=head_dict).json()
lot3_list = [lot3_data['n' + str(ran)] for ran in [1, 2, 3]]

print('{}.{}.{} {} {}-{} {} {}{}{}'.format(
    keno_data["day"], keno_data["month"], keno_data["year"],
    keno_data["draw"], keno_data["lototron"], keno_data["ballset"],
    keno_list, "\n", sorted(keno_list), "\n"))

print('{}.{}.{} {} {}-{} {}'.format(
    lot3_data["day"], lot3_data["month"], lot3_data["year"],
    lot3_data["draw"], lot3_data["lototron"], lot3_data["ballset"],
    lot3_list))
